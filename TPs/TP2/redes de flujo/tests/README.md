# Tests — Traslado de Información Secreta

Este directorio contiene los casos de prueba para validar el correcto funcionamiento del programa `traslado.py`.

## 📁 Estructura de pruebas

Para agregar una nueva prueba, creá una carpeta dentro de `cases` con el nombre `case-X`, donde `X` es el número de caso (por ejemplo, `case-1`, `case-2`, etc).  
Dentro de cada carpeta deben incluirse los siguientes archivos:

- `config.txt` → contiene dos números separados por espacio: `n s`, donde `n` es la cantidad de espías/centros y `s` la capacidad máxima por ciudad.
- `ciudades.txt` → lista de conexiones entre ciudades, una por línea, con el formato `CiudadA,CiudadB`.
- `espias.txt` → lista de espías (primeras `n` líneas) y centros (últimas `n` líneas), cada uno con su ciudad actual: `Nombre,Ciudad`.
- `esperado.txt` → salida esperada del programa. Puede contener múltiples soluciones válidas separadas por `---` si se usa `comparador.py`.

### 📦 Ejemplo de `config.txt`:

- 3 2
Significa: 3 espías/centros, con capacidad máxima 2 espías por ciudad intermedia.

---

## ▶️ Cómo ejecutar las pruebas

### 🧪 Usando el Makefile (Unix/Linux/Git Bash):

```bash
# Ejecutar todas las pruebas
make test

# Ejecutar todas las pruebas desde PowerShell o CMD
.\run_tests.bat