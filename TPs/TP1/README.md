# Trabajo Práctico 1

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.
- Se debe entregar el informe en formato PDF y el código fuente en (.zip) en el aula virtual de la materia.
- El lenguaje de implementación es libre (recomendado: C, C++ o Python). Si se desea utilizar otro, debe pactarse con los docentes.
- Incluir en el informe los requisitos y procedimientos para compilación y ejecución. La ausencia de esta información implica re-entrega.
- El informe debe presentar carátula con nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.
- Incluir las fuentes consultadas en una sección de referencias.
- En caso de re-entrega, agregar un apartado con las correcciones realizadas.

---

## Parte 1: Solitario… en grupo

Considerar el problema “Jugando al solitario” del trabajo práctico 0. Cada participante elaboró una propuesta algorítmica. Deben comparar y responder:

- ¿Todas las propuestas fueron greedy?
- ¿Cuáles fueron las complejidades de cada una? ¿Hay mejores y peores?
- ¿Fueron todas óptimas? Si no, brinde un contraejemplo para las que no. Realice la demostración de optimalidad para una que sí (si ninguna fue óptima, propongan una que lo sea).

---

## Parte 2: Los puentes que se cruzan

Un río separa la ciudad en dos regiones: norte y sur, con “2n” barrios (n por margen). Cada puente une un barrio del norte con uno del sur. Cada barrio solo puede ser parte de una única propuesta. El comité debe determinar la factibilidad de la construcción: no es factible si existen puentes que se cruzan. Si no es posible, informar cuántos cruces existen.

**Datos:**
- Orden de los barrios en cada margen.
- Propuestas: duplas (barrio norte, barrio sur).

**Se pide:**
- Propuesta mediante división y conquista para resolver el problema.
- Ecuación de recurrencia y complejidad (teorema maestro).
- Pseudocódigo.
- Ejemplo de funcionamiento.
- Programa en Python que resuelva el problema.

**Análisis:**  
¿La complejidad del programa es igual a la de la propuesta? Justifique.

**Formato de archivos:**
- El archivo ejecutable debe llamarse `puentes_dq.py`.
- Recibe por parámetro el nombre de un archivo con los barrios ordenados y otro con las propuestas.

**Formato de archivo de barrios:**
```
Barrancas
San Pedro
El hurón
Palo seco
Puente viejo

Cienagas
Don Corleone
Barrio Este
Portuario
Torre verde
```

**Formato de archivo de propuestas:**
```
Puente viejo, Don Corleone
Barrancas, Cienagas
El hurón, Portuario
San Pedro, Barrio Este
Palo seco, Torre verde
```

La salida debe ser un número con la cantidad de cruces.

---

## Parte 3: Maximizando los puentes

Determinar qué puentes construir evitando cruces y maximizando la cantidad de puentes.

**Se pide:**
- Resolver el problema utilizando programación dinámica (definición del subproblema, relación de recurrencia y pseudocódigo).
- Explicar por qué la propuesta funciona.
- Analizar la complejidad espacial y temporal.
- Ejemplo paso a paso.
- Programar la solución.
- Analizar si la complejidad propuesta es igual a la del programa.
- Analizar si el resultado es único. Si no, dar contraejemplo o demostrarlo. ¿Se puede modificar para obtener una solución diferente?

**Formato de archivos:**
- El archivo ejecutable debe llamarse `puentes_pd.py`.
- Recibe los mismos parámetros que el programa de división y conquista.
- Debe mostrar por pantalla: la cantidad de puentes que se pueden construir y los puentes