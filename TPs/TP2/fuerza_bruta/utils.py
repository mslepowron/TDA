from collections import defaultdict

def leer_ofertas(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        lineas = [line.strip() for line in f.readlines()]
    m = int(lineas[0])
    P = {}
    invitados = []
    for linea in lineas[1:]:
        partes = linea.split(',')
        nombre = partes[0]
        ofertas = list(map(int, partes[1:]))
        P[nombre] = ofertas
        invitados.append(nombre)
    return m, P, invitados

def leer_restricciones(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        lineas = [line.strip() for line in f.readlines()]
    E = {}
    for linea in lineas:
        partes = linea.split(',')
        persona = partes[0]
        E[persona] = set(partes[1:]) if len(partes) > 1 else set()
    return E

def leer_ofertas_bb(archivo):
    with open(archivo, 'r') as f:
        lineas = f.read().strip().splitlines()
    m = int(lineas[0])
    invitados = {}
    ofertas = {}
    for linea in lineas[1:]:
        partes = linea.strip().split(',')
        nombre = partes[0]
        ofertas[nombre] = list(map(int, partes[1:]))
        invitados[nombre] = None
    return m, ofertas, invitados

def leer_enemistades_bb(archivo):
    enemistades = defaultdict(set)
    with open(archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) > 1:
                nombre = partes[0]
                enemigos = partes[1:]
                enemistades[nombre].update(enemigos)
    return enemistades
