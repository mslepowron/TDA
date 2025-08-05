import heapq
import sys
from collections import defaultdict, namedtuple
from utils import leer_ofertas_bb, leer_enemistades_bb

Nodo = namedtuple('Nodo', ['asignaciones', 'ganancia_actual', 'invitados_restantes', 'porciones_restantes', 'bound'])

class MaxHeap:
    def __init__(self):
        self.data = []
        self.counter = 0  # contador para desempatar

    def insertar(self, nodo):
        # agregamos un contador como segundo elemento para evitar comparación de dicts
        heapq.heappush(self.data, (-nodo.bound, self.counter, nodo))
        self.counter += 1

    def extraer_max(self):
        return heapq.heappop(self.data)[2]

    def esta_vacio(self):
        return len(self.data) == 0


def costo(ganancia_actual, invitados_restantes, porciones_restantes, ofertas):
    bound = ganancia_actual
    for p in porciones_restantes:
        mejor_oferta = max([ofertas[i][p] for i in invitados_restantes], default=0)
        bound += mejor_oferta
    return bound

def es_valida_asignacion(asignaciones, porcion_actual, invitado, enemistades, m):
    vecinos = {(porcion_actual - 1 + m) % m, (porcion_actual + 1) % m}
    for vecino in vecinos:
        if vecino in asignaciones:
            invitado_vecino = asignaciones[vecino]
            if invitado_vecino is None:
                continue
            if invitado_vecino in enemistades[invitado]:
                return False
    return True

def seleccionar_porcion(porciones_restantes):
    # selecciona la porción con menor índice
    return min(porciones_restantes)

def branch_and_bound(m, invitados, ofertas, enemistades):
    mejor_ganancia = 0
    mejor_asignacion = {}

    todos_invitados = set(invitados.keys())
    todas_porciones = set(range(m))

    asignacion = MaxHeap()
    nodo_raiz = Nodo(
        asignaciones={},
        ganancia_actual=0,
        invitados_restantes=todos_invitados,
        porciones_restantes=todas_porciones,
        bound=costo(0, todos_invitados, todas_porciones, ofertas)
    )
    asignacion.insertar(nodo_raiz)

    while not asignacion.esta_vacio():
        nodo = asignacion.extraer_max()

        if nodo.bound <= mejor_ganancia:
            continue

        if not nodo.porciones_restantes:
            if nodo.ganancia_actual > mejor_ganancia:
                mejor_ganancia = nodo.ganancia_actual
                mejor_asignacion = nodo.asignaciones
            continue

        porcion_actual = seleccionar_porcion(nodo.porciones_restantes)

        #Caso de dejar la porcion vacia

        nueva_asignacion = nodo.asignaciones.copy()
        nueva_asignacion[porcion_actual] = None
        nuevos_invitados = nodo.invitados_restantes
        nuevas_porciones = nodo.porciones_restantes - {porcion_actual}
        nuevo_bound = costo(nodo.ganancia_actual, nuevos_invitados, nuevas_porciones, ofertas)

        nuevo_nodo = Nodo(
            asignaciones=nueva_asignacion,
            ganancia_actual=nodo.ganancia_actual,
            invitados_restantes=nuevos_invitados,
            porciones_restantes=nuevas_porciones,
            bound=nuevo_bound
        )
        asignacion.insertar(nuevo_nodo)

        #Caso de asignarle la porcion a un invitado
        for invitado in nodo.invitados_restantes:
            if es_valida_asignacion(nodo.asignaciones, porcion_actual, invitado, enemistades, m):
                nueva_asignacion = nodo.asignaciones.copy()
                nueva_asignacion[porcion_actual] = invitado

                nueva_ganancia = nodo.ganancia_actual + ofertas[invitado][porcion_actual]

                nuevos_invitados = nodo.invitados_restantes - {invitado}
                nuevas_porciones = nodo.porciones_restantes - {porcion_actual}

                nuevo_bound = costo(nueva_ganancia, nuevos_invitados, nuevas_porciones, ofertas)

                nuevo_nodo = Nodo(
                    asignaciones=nueva_asignacion,
                    ganancia_actual=nueva_ganancia,
                    invitados_restantes=nuevos_invitados,
                    porciones_restantes=nuevas_porciones,
                    bound=nuevo_bound
                )

                asignacion.insertar(nuevo_nodo)

    return mejor_ganancia, mejor_asignacion

def main():
    if len(sys.argv) != 3:
        print("Uso: python subasta_bb.py ofertas.txt restricciones.txt")
        return

    archivo_ofertas = sys.argv[1]
    archivo_restricciones = sys.argv[2]

    m, ofertas, invitados = leer_ofertas_bb(archivo_ofertas)
    enemistades = leer_enemistades_bb(archivo_restricciones)

    ganancia, asignacion = branch_and_bound(m, invitados, ofertas, enemistades)

    print(f"La ganancia máxima a obtener es: {ganancia}")
    
    ganadores_ordenados = [asignacion.get(p, "") for p in sorted(asignacion)] 
    print("Los invitados ganadores son:", ', '.join(i for i in ganadores_ordenados if i is not None))


if __name__ == "__main__":
    main()