#%%
numero_1 = float(input("Inserte el primer número: "))
numero_2 = float(input("Inserte el segundo número: "))
operador = input("Ingrese el tipo de operación: ")
if operador == "+":
    print("Resultado: ", numero_1 + numero_2)
elif operador == "-":
    print("Resultado: ", numero_1 - numero_2)
elif operador == "*":
    print("Resultado: ", numero_1 * numero_2)
elif operador == "/":
    print("Resultado: ", numero_1 / numero_2)
elif operador == "%":
    print("Resultado: ", numero_1 % numero_2)
else:
    print("Ingreso un operador invalido")