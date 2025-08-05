from propuesta_sa import *

# Ejemplo 1: Sin conflictos (caso base óptimo)
inversores = [
    ('A', 100,  []),
    ('B', 200,  []),
    ('C', 150,  []),
]
seleccionados, ganancia_maxima = obtener_mejores_inversores(inversores)
print("\nEjemplo 1")
print("Beneficio:", ganancia_maxima)
print("Seleccionados:", seleccionados)

# Ejemplo 2: Conflictos simples con múltiples soluciones óptimas
inversores = [
    ('A', 100,  ['B']),
    ('B', 200,  ['A', 'C']),
    ('C', 150,  ['B']),
]
seleccionados, ganancia_maxima = obtener_mejores_inversores(inversores)
print("\nEjemplo 2")
print("Beneficio:", ganancia_maxima)
print("Seleccionados:", seleccionados)

# Ejemplo 3: 
inversores = [
    ('A', 150, ['B', 'C', 'D', 'E']),
    ('B', 80, ['A']),
    ('C', 80, ['A']),
    ('D', 80, ['A']),
    ('E', 80, ['A'])
]
seleccionados, ganancia_maxima = obtener_mejores_inversores(inversores)
print("\nEjemplo 3")
print("Beneficio:", ganancia_maxima)
print("Seleccionados:", seleccionados)

# Ejemplo 4: Todos en conflicto entre sí (clique completa)
inversores = [
    ('A', 100, ['B', 'C', 'D', 'E']),
    ('B', 200, ['A', 'C', 'D']),
    ('C', 300, ['A', 'B', 'D']),
    ('D', 200, ['A', 'B', 'C'])
]
conflictos = [('A','B'), ('A','C'), ('A','D'), ('B','C'), ('B','D'), ('C','D')]
seleccionados, ganancia_maxima = obtener_mejores_inversores(inversores)
print("\nEjemplo 4")
print("Beneficio:", ganancia_maxima)
print("Seleccionados:", seleccionados)

# Ejemplo 5: Grafo con conflictos encadenados que da solucion no optima
inversores = [
    ('A', 100, ['B']),
    ('B', 200, ['A', 'C']),
    ('C', 150, ['B', 'D']),
    ('D', 100, ['C', 'E']),
    ('E', 80, ['D'])
]
seleccionados, ganancia_maxima = obtener_mejores_inversores(inversores)
print("\nEjemplo 5")
print("Beneficio:", ganancia_maxima)
print("Seleccionados:", seleccionados)
