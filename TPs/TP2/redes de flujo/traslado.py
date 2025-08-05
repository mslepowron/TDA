import sys
from collections import deque, defaultdict

def leer_archivo_ciudades(path):
    vuelos = []
    with open(path, "r") as file:
        for linea in file:
            partes = linea.strip().split(",")
            if len(partes) != 2:
                raise ValueError(f"Línea inválida en ciudades: '{linea.strip()}' (se esperaba origen,destino)")
            origen, destino = partes
            vuelos.append((origen.strip(), destino.strip()))
    return vuelos

def leer_archivo_espias(path, n):
    espias, centros = [], []
    with open(path, "r") as file:
        lineas = [linea.strip() for linea in file if linea.strip()]
    
    if len(lineas) < 2 * n:
        raise ValueError(f"Se esperaban al menos {2 * n} líneas en '{path}', pero hay {len(lineas)}")

    for i in range(n):
        partes = lineas[i].split(",")
        if len(partes) != 2:
            raise ValueError(f"Línea inválida en espías: '{lineas[i]}' (se esperaba nombre,ciudad)")
        nombre, ciudad = partes
        espias.append((nombre.strip(), ciudad.strip()))
    
    for i in range(n, 2 * n):
        partes = lineas[i].split(",")
        if len(partes) != 2:
            raise ValueError(f"Línea inválida en centros: '{lineas[i]}' (se esperaba nombre,ciudad)")
        nombre, ciudad = partes
        centros.append((nombre.strip(), ciudad.strip()))
    
    return espias, centros

def construir_grafo(vuelos, espias, centros, s):
    grafo = defaultdict(dict)
    ciudades = set()

    for a, b in vuelos:
        ciudades.add(a)
        ciudades.add(b)

    for ciudad in ciudades:
        grafo[f"{ciudad}_in"][f"{ciudad}_out"] = s

    for a, b in vuelos:
        grafo[f"{a}_out"][f"{b}_in"] = s
        grafo[f"{b}_out"][f"{a}_in"] = s

    for nombre, ciudad in espias:
        grafo["fuente"][nombre] = 1
        grafo[nombre][f"{ciudad}_in"] = 1

    for nombre, ciudad in centros:
        grafo[f"{ciudad}_out"][nombre] = s
        grafo[nombre]["sumidero"] = s

    return grafo, ciudades

def bfs(gr_residual, fuente, sumidero, camino_aumento):
    visitado = set()
    queue = deque([fuente])
    camino_aumento.clear()
    camino_aumento[fuente] = None

    while queue:
        u = queue.popleft()
        for v in gr_residual[u]:
            if v not in visitado and gr_residual[u][v] > 0:
                camino_aumento[v] = u
                visitado.add(v)
                if v == sumidero:
                    return True
                queue.append(v)
    return False

def augment(gr_residual, camino_aumento, fuente, sumidero):
    b = float('inf')
    v = sumidero
    while v != fuente:
        u = camino_aumento[v]
        b = min(b, gr_residual[u][v])
        v = u

    v = sumidero
    while v != fuente:
        u = camino_aumento[v]
        gr_residual[u][v] -= b
        gr_residual[v][u] = gr_residual[v].get(u, 0) + b
        v = u

    return b

def ford_fulkerson(G, fuente, sumidero):
    flujo_total = 0
    camino_aumento = {}
    gr_residual = defaultdict(dict)

    for u in G:
        for v in G[u]:
            gr_residual[u][v] = G[u][v]

    while bfs(gr_residual, fuente, sumidero, camino_aumento):
        b = augment(gr_residual, camino_aumento, fuente, sumidero)
        flujo_total += b

    return flujo_total, gr_residual

def armado_de_ruta(grafo_original, grafo_residual, nodo, ciudades_legibles):
    for vecino in grafo_original[nodo]:
        usado = grafo_original[nodo][vecino] - grafo_residual[nodo].get(vecino, 0)
        if usado > 0:
            ciudad = vecino.replace("_in", "").replace("_out", "")
            if ciudad not in ("fuente", "sumidero") and (not ciudades_legibles or ciudad != ciudades_legibles[-1]):
                ciudades_legibles.append(ciudad)
            armado_de_ruta(grafo_original, grafo_residual, vecino, ciudades_legibles)
            break

def reconstruir_rutas(grafo_original, grafo_residual, espias):
    rutas = []
    for nombre, _ in espias:
        usado = grafo_original["fuente"][nombre] - grafo_residual["fuente"].get(nombre, 0)
        if usado > 0:
            ciudades_legibles = []
            armado_de_ruta(grafo_original, grafo_residual, nombre, ciudades_legibles)
            rutas.append(f"{nombre},{','.join(ciudades_legibles)}")
    return rutas

def trasladar(n, s, archivo_ciudades, archivo_espias):
    vuelos = leer_archivo_ciudades(archivo_ciudades)
    espias, centros = leer_archivo_espias(archivo_espias, n)
    grafo, _ = construir_grafo(vuelos, espias, centros, s)
    flujo_max, grafo_residual = ford_fulkerson(grafo, "fuente", "sumidero")

    if flujo_max < n:
        print("Es imposible lograr el objetivo")
    else:
        rutas = reconstruir_rutas(grafo, grafo_residual, espias)
        for ruta in rutas:
            print(ruta)
        return rutas

if __name__ == "__main__":
    try:
        trasladar(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
