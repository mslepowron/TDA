# Consigna

## Lineamientos Basicos

- El trabajo se realizará individualmente.

- Se debe entregar el informe en formato pdf y código fuente en (.zip) en el aula virtual de la materia. Tanto el pdf como los archivos de ambas partes deben estar        comprimidos sin utilizar carpetas para organizarlos.

- El lenguaje de implementación elegido es Python.

- El informe debe presentar carátula con los datos del alumno y fecha de entrega. Debe incluir número de hoja en cada página. El informe no debe superar más de 1 página.

- En caso de re-entrega, entregar luego del informe original un apartado con las correcciones realizadas

## Parte 1

Contamos con una mochila con una capacidad de K kilos y queremos introducir dentro de ellas un subconjunto del conjunto E de “n” elementos con el objetivo de maximizar la ganancia. Cada elemento i tiene un peso de ki kilos y un valor de vi. Los elementos NO pueden ser divididos, pero es posible incluir mas de una vez al mismo elemento. El peso total seleccionado no puede superar la capacidad de la mochila.

Nos brindan dos estrategias para resolver el problema:

```bash
Algoritmo mochila A:
```
```bash
def mochila_algoritmo_A(capacidad_mochila, elementos):
	ordenar los elementos de mayor a menor segun valor
	por cada elemento en elementos:
    		Mientras el elemento entra en la mochila:
    			agregar elemento a la mochila
	devolver valor total en mochila
```

```bash
Algoritmo mochila B:
```
```bash
def mochila_algoritmo_B(capacidad_mochila, elementos):
	obtener el valor por kilo de cada elemento
	ordenar los elementos de mayor a menor segun el valor por kilo
	por cada elemento en elementos:
		Mientras el elemento entra en la mochila:
			agregar elemento a la mochila
	devolver valor total en mochila
```

Estos algoritmos se pueden ejecutar en mi compiler.

Se pide:
Encontrar un contraejemplo para los siguientes algoritmos que buscan solucionar el problema de manera óptima. El mismo debe presentarse con el formato indicado a continuación:

Entregar dos archivos llamados “mochilaA.txt” y “mochilaB.txt” con el siguiente formato
```bash
8
(5,10),
(2,3),
(1,1)
```
Donde la primera línea indica la capacidad de la mochila, y el resto son elementos formados por la tupla (peso, valor)

## Parte 2

Contamos con cartas numeradas del 1 al “n” mezcladas en un orden desconocido. No podemos modificar ese orden ni observar que cartas hay, excepto la que se encuentra arriba. Debemos iterativamente tomar la carta superior, observarla y apilarla. Una carta puede formar una pila nueva o ubicarse en una existente. Para ubicarla en una existente debe ser menor a la carta superior de esa pila. Una vez ubicada la carta, no se puede mover y pasa a ser la carta superior. El objetivo es ubicar todas las cartas en la menor cantidad de pilas posible.

Se pide:
Presentar un programa en python que resuelva el problema. Debe cumplir AL PIE DE LA LETRA el formato de entrada y salida según se detalla posteriormente.

- Indicar qué estructuras de datos utiliza para su programa.
- Indicar la complejidad temporal y espacial del programa (sin análisis).
- Explicar en una oración la estrategia greedy.
- Definir en una oración cuál es el óptimo local
- Formato del programa:
- El archivo a ejecutar se debe llamar main.py Debe recibir por parámetro el nombre de un archivo que contenga las cartas mezcladas. El formato del archivo de cartas debe ser texto. Cada línea del archivo corresponde a una carta. Por ejemplo:

```bash
1
4
10
7
2
5
9
3
8
6
```

La salida del programa debe ser por pantalla y solo contener un número con la cantidad de pilas construidas. Formato de ejecución del programa: ```bash main.py archivo.txt```