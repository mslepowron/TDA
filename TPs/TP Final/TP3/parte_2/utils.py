from grafo import Grafo

import sys
import random
import math

'''
Toma por parámetro el nombre de un archivo donde cada línea debe ser de la forma:

ID_INVERSOR,GANANCIA,E1,E2,E2,..,En

En caso de haber enemistades se coloca una segunda coma luego de la ganancia y de allí en
adelante se esperan los enemigos de ID_INVERSOR.

En caso de no haber enemistades la línea quedaría de la siguiente forma:

ID_INVERSOR,GANANCIA
'''
def procesar_archivo(archivo):
    inversores = []
    
    with open(archivo) as f:
        for linea in f:
            info = linea.strip().split(",")
        
            # Cada linea del archivo contendrá al menos una coma, es decir, el identificador del inversor y la ganancia que puede aportar
            inversor = info[0]
            ganancia = float(info[1])
            enemigos = []
            
            if len(info) > 2:
                enemigos = info[2:]
            
            info_inversor = (inversor, ganancia, enemigos)
            inversores.append(info_inversor)
    
    return inversores

'''
Toma por parámetro un arreglo donde los elementos son tuplas de la forma (inversor, ganancia, enemigos).
Devuelve un grafo donde cada vértice corresponde a un inversor y las adyacencias representan enemistades.
'''
def construir_grafo(inversores):
    G = Grafo(dirigido=False)
    ganancias = dict()
    
    for inv in inversores:
        inversor = inv[0]
        ganancia_inversor = inv[1]
        G.agregar_vertice(inversor)
        ganancias[inversor] = ganancia_inversor

    for inv in inversores:
        inversor = inv[0]
        enemigos = inv[2]
        for e in enemigos:
            G.agregar_arista(inversor, e)
    
    return G, ganancias