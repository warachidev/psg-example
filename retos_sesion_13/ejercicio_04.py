# %%
while True:
    palabra = input("Ingresar una palabra")
    palabra = palabra.lower()
    if (palabra == "salir"):
        break
    if (palabra[::1] == palabra[::-1]):
        print(palabra, " : Es palindromo")
    else:
        print(palabra, " : No ess palindromo")
print("Fin ")