# Trabajo Práctico 2

## Lineamientos básicos

- El trabajo se realizará en grupos de cinco personas.
- Se debe entregar el informe en formato PDF y el código fuente en (.zip) en el aula virtual de la materia.
- El lenguaje de implementación es libre (recomendado: C, C++ o Python). Si se desea utilizar otro, debe pactarse con los docentes.
- Incluir en el informe los requisitos y procedimientos para compilación y ejecución. La ausencia de esta información implica re-entrega.
- El informe debe presentar carátula con nombre del grupo, datos de los integrantes, fecha y número de entrega. Debe incluir número de hoja en cada página. No debe superar las 25 páginas + carátula + índice + referencias.
- Incluir las fuentes consultadas en una sección de referencias.
- En caso de re-entrega, agregar un apartado con las correcciones realizadas.

---

## Parte 1: La subasta de pizza

El restaurante “Altezzoso” realiza una subasta de una pizza XXXL cortada en “m” porciones entre “n” invitados (n > m). Cada invitado tiene un presupuesto de “p” liras para ofertar por las porciones. La mesa es circular y cada invitado solo puede acceder a una porción. Algunos invitados no quieren sentarse junto a otros, por lo que deben evitarse ciertas asignaciones.

Se debe determinar la asignación de porciones a invitados para maximizar la ganancia, cumpliendo las restricciones.

**Soluciones propuestas:**
- Backtracking: Determinar todas las ubicaciones factibles (sin considerar rotaciones), y calcular la ganancia de cada rotación.
- Branch and Bound: Proponer una alternativa utilizando esta técnica.

**Se pide:**
- Explicar brevemente cada solución. Definir función costo y límite cuando corresponda.
- Dar pseudocódigo y estructuras de datos a utilizar.
- Analizar y comparar la complejidad temporal y espacial de ambas soluciones.
- Brindar un ejemplo simple paso a paso.
- Programar ambas propuestas.
- Determinar si los programas tienen la misma complejidad que la propuesta teórica.

**Formato de archivos:**
- Los programas deben llamarse `subasta_bt` y `subasta_bb`.
- Reciben por parámetro dos archivos: uno de ofertas y otro de restricciones.

**Ejemplo de archivo de ofertas:**
```
4
Elon,10,0,10,5
Steve,5,5,5,10
Mark,7,7,7,4
Jeff,0,0,25,0
Larry,0,15,5,5
Bill,8,7,10,0
```

**Ejemplo de archivo de restricciones:**
```
Elon,Jeff,Larry
Steve,Elon
Mark,Bill,Larry
Jeff,Elon
Larry
Bill,Mark
```

**Formato de salida:**
```
La ganancia máxima a obtener es: [ganancia]
Los invitados ganadores son: [ganadores separados por coma, ordenados por número de porción]
```

---

## Parte 2: El traslado de información secreta

Hay “n” agentes secretos en diferentes ciudades, cada uno debe llevar información a uno de los “n” centros de investigación en otras ciudades. Usan una red de vuelos bidireccionales y pueden hacer escalas en ciudades seguras. No más de “s” agentes pueden pasar por la misma ciudad.

**Se pide:**
- Propuesta mediante redes de flujo. Explicar la idea.
- Presentar pseudocódigo.
- Análisis de optimalidad.
- Análisis de complejidad temporal y espacial.
- Programar la solución y comparar la complejidad teórica con la práctica.
- Analizar si la solución puede expresarse como una reducción polinomial.

**Formato de archivos:**
- El programa debe llamarse `traslado`.
- Recibe por parámetros dos números (`n` y `s`) y dos archivos (ciudades/vuelos y espías/centros).

**Ejemplo de archivo de ciudades y vuelos:**
```
A,B
A,D
A,E
B,C
C,D
C,E
D,E
```

**Ejemplo de archivo de espías y centros:**
```
Espia 1,A
Espia 2,B
Centro 1,C
Centro 2,D
```

**Formato de salida:**
- Si no es posible:  
  `Es imposible lograr el objetivo`
- Si es posible:  
  `[ruta de cada espía, separada por coma]`

---

## Parte 3: Las 2 jornadas de capacitación

Una nueva empresa se creó por la fusión de varias existentes. Por lo tanto se realizaron 2 jornadas de capacitación para todos sus equipos de desarrollo. Entre su personal existen “m” tipos de profesionales. Cada equipo de trabajo tiene como máximo 1 integrante con cada tipo de profesión entre sus miembros. Actualmente tienen “n” equipos de trabajo. En cada jornada pueden asistir no más de “p” personas por restricciones edilicias. Desean invitar a algunos tipos de profesiones para que vayan un día y el resto el otro. Una restricción adicional es que no puede pasar que todos los miembros de un equipo de trabajo asista todos juntos en un mismo día (para fomentar la integración).

**Se pide:**
- Demostrar que, dada una posible solución que nos brindan, se puede fácilmente determinar si se puede cumplir o no con la tarea solicitada.

- Demostrar que si desconocemos si es posible lograr una solución, es difícil poder afirmar que existe. Utilizar para eso el problema “Set splitting problem” (suponiendo que sabemos que este es NP-C).

- Demostrar que el problema “Set splitting problem” pertenece a NP-C. (Para la demostración se le solicita investigar. La misma se puede realizar partiendo desde “3-SAT” y pasando por “NAE-3-SAT”).

- Una persona afirma tener un método eficiente para responder si es posible o no cualquiera sea la instancia. Utilizando el concepto de transitividad y la definición de NP-C explique qué ocurriría si se demuestra que la afirmación es correcta.

- Un tercer problema al que llamaremos X se puede reducir polinomialmente al problema de “Las 2 jornadas de capacitación”, qué podemos decir acerca de su complejidad?