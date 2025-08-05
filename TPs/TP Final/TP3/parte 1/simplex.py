from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

model = LpProblem(name="proyectos", sense=LpMaximize)

xA = LpVariable(name="xA", lowBound=0)
xB = LpVariable(name="xB", lowBound=0)
xC = LpVariable(name="xC", lowBound=0)

model += 200 * xA + 100 * xB + 300 * xC, "Ganancia_total"

model += xA + xB + 3 * xC <= 17, "Ingenieros"
model += 3 * xA + 2 * xB + 2 * xC <= 11, "Diseñadores"

model.solve()

# Imprimir resultados
print(f"Estado: {model.status}, {LpStatus[model.status]}")
print(f"xA = {xA.value()}")
print(f"xB = {xB.value()}")
print(f"xC = {xC.value()}")
print(f"Ganancia total = {value(model.objective)}")
