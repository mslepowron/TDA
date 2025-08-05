import sys
from utils import leer_ofertas, leer_restricciones

def ubicaciones_factibles(invitados, enemigos, ofertas_porcion, n, m):
    ubi_factibles = []
    invitados_usados = set()
    
    obtener_ubicaciones(invitados, enemigos, [], invitados_usados, 0, n, m, ubi_factibles)
    return maxima_ganancia_con_rotaciones(ubi_factibles, ofertas_porcion, m)

#Funcion de backtracking
def obtener_ubicaciones(invitados, enemigos, uParcial, invitados_usados, porcion, n, m, uFactibles):
    if porcion == m:
        if es_factible_circular(uParcial, enemigos):
            uFactibles.append(uParcial.copy())
        return

    for i in range(n):
        invitado = invitados[i]
        if invitado in invitados_usados:
            continue
        if not puedo_ubicarlo(uParcial, invitado, enemigos):
            continue
        uParcial.append(invitado)
        invitados_usados.add(invitado)
        obtener_ubicaciones(invitados, enemigos, uParcial, invitados_usados, porcion + 1, n, m, uFactibles)
        uParcial.pop()
        invitados_usados.remove(invitado)

    # otro caso base: no ubico a nadie en esta posición (asiento vacío)
    uParcial.append(None)
    obtener_ubicaciones(invitados, enemigos, uParcial, invitados_usados, porcion + 1, n, m, uFactibles)
    uParcial.pop()


def es_factible_circular(ubicacion_parcial, enemigos):
    if len(ubicacion_parcial) < 2:
        return True
    
    primer_invitado = ubicacion_parcial[0]
    ultimo_invitado = ubicacion_parcial[-1]

    if primer_invitado is None or ultimo_invitado is None:
        return True
    if primer_invitado in enemigos.get(ultimo_invitado, set()) or ultimo_invitado in enemigos.get(primer_invitado, set()):
        return False
    return True

def puedo_ubicarlo(ubicaciones_parcial, invitado, enemigos):
    if len(ubicaciones_parcial) == 0:
        return True
    
    invitado_anterior = ubicaciones_parcial[-1]

    if invitado_anterior is None:
        return True
    if invitado in enemigos.get(invitado_anterior, set()) or invitado_anterior in enemigos.get(invitado, set()):
        return False
    return True

def maxima_ganancia_con_rotaciones(ubicaciones_factibles, ofertas_porciones, m):
    gananciaMaxima = 0
    asignacionOptima = []

    for ubicacion in ubicaciones_factibles:
        for i in range(m):
            rotada = rotar(ubicacion, i)
            ganancia = 0
            for j in range(m):
                invitado = rotada[j]
                if invitado is not None:
                    ganancia += ofertas_porciones[invitado][j]
            if ganancia > gananciaMaxima:
                gananciaMaxima = ganancia
                asignacionOptima = rotada.copy()

    return gananciaMaxima, asignacionOptima

def rotar(ubicacion, k):
    return ubicacion[k:] + ubicacion[:k]


def main():
    if len(sys.argv) != 3:
        print("Uso: python3 subasta_bt.py ofertas.txt restricciones.txt")
        sys.exit(1)

    archivo_ofertas = sys.argv[1]
    archivo_restricciones = sys.argv[2]

    m, oferta_porcion, invitados = leer_ofertas(archivo_ofertas)
    enemigos = leer_restricciones(archivo_restricciones)
    n = len(invitados)

    ganancia, asignacion = ubicaciones_factibles(invitados, enemigos, oferta_porcion, n, m)

    print("La ganancia máxima a obtener es:", ganancia)
    print("Los invitados ganadores son:", ', '.join(i for i in asignacion if i is not None))

if __name__ == "__main__":
    main()