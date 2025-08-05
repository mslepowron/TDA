# TP Final

## Parte 1: Personal para proyectos
Una consultora ofrece personal calificado para 3 tipos de proyectos. Cada proyecto requiere ingenieros y diseñadores. Actualmente tiene en su nómina 17 y 11 de estos profesionales respectivamente. El proyecto tipo “A” requiere 1 ingeniero y 3 diseñadores. El proyecto tipo “B” requiere 1 ingeniero y 2 diseñadores. Finalmente el proyecto tipo “C” requiere 3 y 2. Por cada proyecto gana respectivamente 200, 100 y 300 (en millones de pesos). Desean determinar cuántos proyectos y de qué tipo aceptar para maximizar las ganancias.

Se pide:

1. Expresar y explicar el problema como un problema de programación lineal.

2. Explicar como resolver el problema utilizando Simplex. Brindar pseudocódigo y explicación de su propuesta. Expresar como se representa la solución.

3. Analizar la complejidad temporal y espacial de cada uno de los pasos de su solución.

4. Presente paso a paso la solución del problema. Presente esquemáticamente cada iteración del algoritmo. Indique qué decisiones se toma en cada uno de estos y los cálculos realizados.

4. Analizar la solución obtenida. ¿Corresponde a la solución óptima del problema? Según la naturaleza del problema, ¿lo puede encontrar en tiempo polinomial? Justificar.

5. Investigar la aplicación de Branch and Bound dentro de programación lineal entera. Explique cómo funciona paso a paso. Brinde pseudocódigo. ¿Lo puede utilizar en el problema? En caso afirmativo desarrolle como hacerlo paso a paso.

6. Programe su propuesta. Puede utilizar librerías para Simplex. (Ejemplos: ALGLIB o PulP).

## Parte 2: Buscando una solución aceptable.

Para el desarrollo de un proyecto estamos buscando inversores. Contamos con una preselección de “n” de estos. cada uno de ellos nos prometió aportar cierta cantidad de dinero (este valor no necesariamente es igual para cada inversor). Nos gustaría aceptar a todos. Sin embargo, algunos inversores se niegan a participar si otros están. Nos gustaría determinar a cuáles aceptar para maximizar el dinero total para la inversión

Se pide:

1. Analizar el problema y determinar si es posible resolverlo de forma eficiente.

2. Proponer 2 algoritmos heurísticos/randomizados o de aproximación para resolverlo. Explicar cómo funcionan

3. Brindar pseudocódigo y análisis completo del mismo (análisis de complejidad temporal, espacial, optimalidad, grado de aproximación, según corresponda al tipo de solución).

4. Realizar su programa y brindar varios ejemplos para su ejecución

5. Realizar un análisis empírico de sus soluciones. ¿Puede determinar en qué casos es mejor uno que el otro?

## Parte 3: Automatas finitos

Los siguientes lenguajes corresponden a la intersección (expresado mediante la conjunción “y”) de dos lenguajes más simples (los símbolos de los mismos corresponden a los números 0 y 1) :

```bash
lenguaje "a": {w| w (tiene dentro suyo la subcadena “1011”) y (tiene un número par de “0”) } 
lenguaje "b": {w| w (toda posición impar es un “1”) y (termina con 3 “1”)}
```

Ejemplos:
```bash
a: “101110”, “1010111”
b: “1010111”, “101010111”
```

Se pide:

1. Construir un autómata finito determinista (AFD) de forma formal para cada uno de los lenguajes simples.

2. Basándose en los autómatas construidos generar de forma formal los dos autómatas finitos determinísticos de los lenguajes más complejos.

3. Representar cada uno de los AFD mediante su representación gráfica

4. Para cada AFD Brindar un ejemplo de una cadena que acepta y otra que rechaza. Explicar cómo determinar su autómata si es aceptado o rechazado paso a paso.