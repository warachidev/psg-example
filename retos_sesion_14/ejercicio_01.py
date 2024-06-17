# %%
def calcular_promedio(calificaciones):
    return (sum(x for x in calificaciones)) / len(calificaciones)

calificaciones_juan = [20,40,60,51,13]
print("promedio: ", calcular_promedio(calificaciones_juan))
# %%
