import sys
from utils import *

def evaluar_factibilidad_pd(puentes_propuestos):
    n = len(puentes_propuestos)
    opt = [1 for _ in range(n)]
    anterior = [-1 for _ in range(n)]
    ix_ultimo_ubicado = 0
    
    # Construímos los óptimos.
    for i in range(1, n):
        for j in range(i):
            if puentes_propuestos[j][BARRIO_SUR] < puentes_propuestos[i][BARRIO_SUR] and opt[j] + 1 > opt[i]:
                anterior[i] = j
                opt[i] = opt[j] + 1
                if opt[i] > opt[ix_ultimo_ubicado]:
                    ix_ultimo_ubicado = i
    
    # Reconstruímos la solución.
    i = ix_ultimo_ubicado
    cant_opt = opt[i]
    res = []
    while i != -1:
        res.append(puentes_propuestos[i])
        i = anterior[i]
        
    res.reverse()
    return cant_opt, res
    
def main(argv):
    archivo_barrios = argv[1]
    orden_barrios_norte, orden_barrios_sur, ix_barrio_norte, ix_barrio_sur = obtener_orden_barrios(archivo_barrios)

    archivo_propuestas = argv[2]
    puentes_propuestos = obtener_propuestas(archivo_propuestas, orden_barrios_norte, orden_barrios_sur)

    cant_opt_propuestas, propuestas_elegidas = evaluar_factibilidad_pd(puentes_propuestos)
    
    # Al momento de imprimir las propuestas elegidas, uso los nombres de los barrios.
    propuestas_elegidas_nombres = []
    for ix_bn, ix_bs in propuestas_elegidas:
        barrio_norte = ix_barrio_norte[ix_bn]
        barrio_sur = ix_barrio_sur[ix_bs]
        propuesta = (barrio_norte, barrio_sur)
        propuestas_elegidas_nombres.append(propuesta)
    
    print(cant_opt_propuestas)
    print(propuestas_elegidas_nombres)
    return


if __name__ == "__main__":
    main(sys.argv)