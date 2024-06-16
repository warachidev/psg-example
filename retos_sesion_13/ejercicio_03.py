# %%
estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]
for estudiante, nota in estudiantes:
    if(nota>50):
        print("Felicidades: " + estudiante)