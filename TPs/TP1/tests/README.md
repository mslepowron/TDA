# Tests

Para agregar nuevas pruebas, se debe agregar una nueva carpeta dentro de `cases` con el nombre de la prueba. Dentro de esta carpeta, se deben agregar los siguientes archivos:

- `barrios.txt`
- `propuestas.txt`
- `esperado-dq.txt`
- `esperado-pd.txt`

Para ejecutar las pruebas:

```bash
# Correr todos los test
$ make test

# División y conquista
$ make test_dq

# Programación dinámica
$ make test_pd
```
