# %%
def operacion_suma(num1, num2): return num1 + num2
def operacion_resta(num1, num2): return num1 - num2
def operacion_multiplicacion(num1, num2): return num1 * num2
def operacion_division(num1, num2): return num1 / num2

def calculadora_flexible(num1, num2, operaciones):
    for operacion in operaciones:
        if (operacion == "suma"):
            print ("Suma: ", operacion_suma(num1, num2))
        elif (operacion == "resta"):
            print ("Resta: ", operacion_resta(num1, num2))
        elif (operacion == "multiplicacion"):
            print ("Multiplicación: ", operacion_multiplicacion(num1, num2))
        elif (operacion == "division"):
            print ("División: ", operacion_division(num1, num2))
            
calculadora_flexible(1,2,["suma", "resta", "multiplicacion", "division"])
calculadora_flexible(2,2,["suma", "multiplicacion"])
calculadora_flexible(4,2,["resta", "division"])
calculadora_flexible(10,1,["suma", "resta"])
# %%
