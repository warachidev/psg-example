# %%
mochilero_a = {"París", "Londres", "Nueva York", "Tokio", "Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina","Brasil","Panama","Bolivia"}
print(mochilero_a)
print(mochilero_b)

lugares_no_visitados_a = mochilero_b - mochilero_a
print("Lugares que no visito el mochilero A: ", lugares_no_visitados_a)

lugares_no_visitados_b = mochilero_a - mochilero_b
print("Lugares que no visito el mochilero B: ", lugares_no_visitados_b)
# %%

lugares_en_comun = mochilero_a & mochilero_b
print("Lugares que ambos mochileros visitaron: ", lugares_en_comun)