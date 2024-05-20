# %%
platos_anita = {"Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"}
platos_pepito = {"Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"}
print("Anita: ", len(platos_anita)," ",platos_anita)
print("Pepito: ", len(platos_pepito)," ",platos_pepito)
lista_de_platos = platos_anita | platos_pepito
print("Lista de Platos: ", len(lista_de_platos)," ",lista_de_platos)
platos_en_comun = platos_anita & platos_pepito
print(platos_en_comun)
print("Platos en comun es mayor al 50% ? ",(len(platos_en_comun) >= len(platos_anita)-len(platos_en_comun)) and len(platos_en_comun) >= len(platos_pepito)-len(platos_en_comun))