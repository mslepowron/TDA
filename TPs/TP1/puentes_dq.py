import sys
from utils import *

def evaluar_factibilidad(puentes_propuestos):
    return _evaluar_factibilidad(puentes_propuestos, 0, len(puentes_propuestos) - 1)[1]

def _evaluar_factibilidad(puentes_propuestos, ini, fin):
    if fin <= ini:
        return [puentes_propuestos[ini]], 0
    
    m = (ini + fin) // 2
    
    izq, cruz_izq = _evaluar_factibilidad(puentes_propuestos, ini, m)
    der, cruz_der = _evaluar_factibilidad(puentes_propuestos, m + 1, fin)
    
    return merge_puentes(izq, der, cruz_izq + cruz_der)

def merge_puentes(izq, der, cruzados):
    i = j = 0
    res = []
    
    while i < len(izq) and j < len(der):
        prop_izq = izq[i]
        prop_der = der[j]
        if prop_izq[BARRIO_SUR] <= prop_der[BARRIO_SUR]:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[j])
            cruzados += len(izq) - i
            j += 1
    
    res.extend(izq[i:])
    res.extend(der[j:])
    
    return res, cruzados

def main(argv):
    archivo_barrios = argv[1]
    orden_barrios_norte, orden_barrios_sur, _, _ = obtener_orden_barrios(archivo_barrios)

    archivo_propuestas = argv[2]
    puentes_propuestos = obtener_propuestas(archivo_propuestas, orden_barrios_norte, orden_barrios_sur)

    cant_props_cruzadas = evaluar_factibilidad(puentes_propuestos)
    print(cant_props_cruzadas)
    return


if __name__ == "__main__":
    main(sys.argv)