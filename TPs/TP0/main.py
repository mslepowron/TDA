import sys

READ = 'r'
ERROR = 1

def apilar_cartas(archivo_cartas):
    with open(archivo_cartas, READ) as archivo:
        cartas = [int(linea.strip()) for linea in archivo]

    pilas_cartas = []

    for carta in cartas:
        carta_apilada = False
        i = 0
        while i < len(pilas_cartas):
            if carta < pilas_cartas[i][len(pilas_cartas[i]) - 1]:
                pilas_cartas[i].append(carta)
                carta_apilada = True
                break  # Encontre una pila para poner mi carta
            i += 1

        if not carta_apilada:
            pilas_cartas.append([carta])  # Creo una nueva pila
    
    print(len(pilas_cartas))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(ERROR)
    
    archivo_cartas = sys.argv[1]
    apilar_cartas(archivo_cartas)