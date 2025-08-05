BARRIO_NORTE = 0
BARRIO_SUR = 1

def obtener_orden_barrios(file):
    with open(file) as f:
        orden_barrios_norte = {}
        ix_barrio_norte = {}
        i = 0
        for linea in f:
            if linea in ['\n', '\r\n']:
                break
            orden_barrios_norte[linea.strip()] = i
            ix_barrio_norte[i] = linea.strip()
            i += 1
        
        orden_barrios_sur = {}
        ix_barrio_sur = {}
        j = 0
        for linea in f:
            if linea in ['\n', '\r\n']:
                break
            orden_barrios_sur[linea.strip()] = j
            ix_barrio_sur[j] = linea.strip()
            j += 1
    
    return orden_barrios_norte, orden_barrios_sur, ix_barrio_norte, ix_barrio_sur

def obtener_propuestas(file, orden_barrios_norte, orden_barrios_sur):
    propuestas = []
    with open(file) as f:
        for linea in f:
            propuesta = linea.strip().split(", ")
            propuestas.append((orden_barrios_norte[propuesta[BARRIO_NORTE]], orden_barrios_sur[propuesta[BARRIO_SUR]]))
    return sorted(propuestas, key=lambda x: x[0])