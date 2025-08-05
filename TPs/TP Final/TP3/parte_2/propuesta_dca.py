from utils import *

def greedy_densidad(grafo, ganancias):
    """
    Algoritmo heurístico basado en densidad conflicto-aporte.
    Recibe:
        - grafo: objeto Grafo
        - ganancias: diccionario {inversor: ganancia}
    Devuelve:
        - beneficio_total: suma de aportes aceptados
        - seleccionados: conjunto de inversores elegidos
    """
    densidad = {
        v: ganancias[v] / (len(grafo.adyacentes(v)) + 1)
        for v in grafo
    }

    ordenados = sorted(grafo, key=lambda v: -densidad[v])
    seleccionados = set()
    beneficio_total = 0

    for v in ordenados:
        if all(w not in seleccionados for w in grafo.adyacentes(v)):
            seleccionados.add(v)
            beneficio_total += ganancias[v]

    return beneficio_total, seleccionados

def obtener_mejores_inversores(info_inversores):
    grafo, ganancias = construir_grafo(info_inversores)
    beneficio_total, seleccionados = greedy_densidad(grafo, ganancias)
    return seleccionados, beneficio_total

def main(argv):
    if len(argv) < 2:
        print("Uso: python3 propuesta_dca.py ejemplo.txt")
        return

    archivo = argv[1]
    info_inversores = procesar_archivo(archivo)
    seleccionados, ganancia_maxima = obtener_mejores_inversores(info_inversores)

    print("La mejor selección de inversores encontrada fue:")
    print("Seleccionados:", seleccionados)
    print("Ganancia total:", ganancia_maxima)

if __name__ == "__main__":
    import sys
    main(sys.argv)
