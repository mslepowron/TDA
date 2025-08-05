import sys

def leer_bloques(path):
    with open(path, "r", encoding="utf-8") as f:
        bloques = f.read().strip().split("\n---\n")
        return [sorted(b.strip().splitlines()) for b in bloques]

def leer_salida(path):
    with open(path, "r", encoding="utf-8") as f:
        return sorted(line.strip() for line in f if line.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python comparador.py esperado.txt salida.txt")
        sys.exit(1)

    esperado_path = sys.argv[1]
    salida_path = sys.argv[2]

    try:
        bloques = leer_bloques(esperado_path)
        salida = leer_salida(salida_path)

        for i, bloque in enumerate(bloques):
            if salida == bloque:
                print(f"✔ Coincide con solución válida #{i+1}")
                sys.exit(0)

        print("❌ Ninguna solución válida coincide con la salida.")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error de comparación: {e}")
        sys.exit(1)
