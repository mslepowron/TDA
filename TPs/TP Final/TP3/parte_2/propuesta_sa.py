from utils import *

T_0 = 5000  # Temperatura inicial
M = 5000  # Cantidad de iteraciones a realizar
C = 0.99     # Constante de enfriamiento

'''
A partir de la información de los distintos inversores construye el grafo y aplica Simulated Annealing para 
buscar el conjunto de inversores que represente la mayor ganancia posible respetando las restricciones del problema.
'''
def obtener_mejores_inversores(inversores):
    G, ganancias = construir_grafo(inversores)
    s_max = simulated_annealing(G, ganancias)
    return s_max, fc(s_max, ganancias)

def simulated_annealing(G, ganancias):
    vertices = G.obtener_vertices()
    v = random.choice(vertices)
    
    s_max = set()
    s = set()
    s.add(v)
    sc = set(vertices)
    sc.remove(v)
    
    it = 0
    T = T_0
    
    s_max = set(s)
    
    while it < M:
        sv, sc = elegir_estado_vecino(s, sc, G)
        s = elegir_nuevo_estado_actual(T, s, sv, ganancias)
        
        if fc(s, ganancias) > fc(s_max, ganancias):
            s_max = set(s)
        
        T = T * C
        it += 1
        
    return s_max

'''
Elige aleatoriamente si agregar o eliminar un vértice del estado actual, actualizando las estructuras empleadas
en función de la decisión tomada y contemplando un vértice al azar.
'''
def elegir_estado_vecino(s, sc, G):
    sv = set(s)
    op = random.choice(['remove', 'add'])
    
    if op == 'remove' and len(sv) > 0: # Hay vértices por quitar.
        v = random.choice(list(sv))
        sv.remove(v)
        sc.add(v)
    
    if op == 'add' and len(sc) > 0: # Hay vértices por agregar.
        v = random.choice(list(sc))
        puedo_agregarlo = True
        for w in G.adyacentes(v):
            if w in sv:
                puedo_agregarlo = False
                break
        if puedo_agregarlo:
            sc.remove(v)
            sv.add(v)
    
    return sv, sc
    
'''
Calcula para ambos estados el valor de la función costo, si el estado vecino brinda una mayor ganancia
entonces lo elige y lo devuelve, en caso contrario decide mediante X si elegir el estado vecino o no.
'''
def elegir_nuevo_estado_actual(T, s, sv, ganancias):
    c = fc(s, ganancias)
    cv = fc (sv, ganancias)
    
    if cv > c:
        return sv
    
    r = random.random()
    exp = (cv - c) / T
    
    if r < math.e ** exp:
        #print(f"Retornamos al VECINO: {list(sv)}")
        return sv
    #print(f"Retornamos al ACTUAL: {list(s)}")
    return s

'''
Dado un estado devuelve la sumatoria de las ganancias que aportan los inversores que lo componen.
'''
def fc(estado, ganancias):
    sum = 0
    for elem in estado:
        sum += ganancias[elem]
    return sum

def main(argv):
    archivo = argv[1]
    info_inversores = procesar_archivo(archivo)
    s_max, g_max = obtener_mejores_inversores(info_inversores)
    print(f"La mejor selección de inversores encontrada fue: {s_max}")
    print(f"La ganancia que representa seleccionarlos es: {g_max}")
    return


if __name__ == "__main__":
    main(sys.argv)
