
#!/usr/bin/env python3
"""Ejecuta todas las instancias *.txt del directorio actual con ambos algoritmos.
Genera un archivo CSV con los resultados.
"""
import os
import csv
import time
from propuesta_sa import obtener_mejores_inversores as run_sa
from propuesta_dca import obtener_mejores_inversores as run_greedy

def cargar_inversores(path):
    datos = []
    with open(path, encoding="utf-8") as f:
        for i, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            partes = linea.split(";")
            if len(partes) != 3:
                print(f"⚠️  Línea inválida en {path}, línea {i}: '{linea}'")
                continue
            nombre, aporte, conflictos = partes
            try:
                aporte = int(aporte)
            except ValueError:
                print(f"⚠️  Aporte inválido en {path}, línea {i}: '{aporte}'")
                continue
            conflictos = [c.strip() for c in conflictos.split(",") if c.strip()]
            datos.append((nombre.strip(), aporte, conflictos))
    return datos

def main():
    folder = "instancias"
    archivos = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".txt")]
    resultados = []
    for archivo in archivos:
        inversores = cargar_inversores(archivo)
        t0 = time.perf_counter()
        sel_g, val_g = run_greedy(inversores)
        tg = (time.perf_counter() - t0) * 1000

        t0 = time.perf_counter()
        sel_sa, val_sa = run_sa(inversores)
        tsa = (time.perf_counter() - t0) * 1000

        resultados.append({
            "archivo": archivo,
            "ganancia_greedy": val_g,
            "ganancia_sa": val_sa,
            "mejor": "Greedy" if val_g >= val_sa else "SA",
            "empate": val_g == val_sa,
            "tiempo_greedy_ms": round(tg, 2),
            "tiempo_sa_ms": round(tsa, 2),
            "inversores_greedy": ",".join(sorted(sel_g)),
            "inversores_sa": ",".join(sorted(sel_sa)),
        })

    with open("resultados_ejecucion.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
        writer.writeheader()
        writer.writerows(resultados)

    print("✅ Resultados guardados en resultados_ejecucion.csv")

if __name__ == "__main__":
    main()
