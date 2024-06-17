# %%
def operacion_suma(num1, num2): 
    try:
        print ("Suma: ",  int(num1) + int(num2))
    except Exception as e:
        print(" Error: ", e)
    
def operacion_resta(num1, num2): 
    try:
        print ("Resta: ", int(num1) - int(num2))
    except Exception as e:
        print(" Error: ", e)
    
def operacion_multiplicacion(num1, num2): 
    try:
        print ("Multiplicación: ",  int(num1) * int(num2))
    except Exception as e:
        print(" Error: ", e)
    
def operacion_division(num1, num2): 
    try:
        print ("División: ",  int(num1) / int(num2))
    except Exception as e:
        print(" Error: ", e)
    

def calculadora_flexible(num1, num2, operaciones):
    for operacion in operaciones:
        if (operacion == "suma"):
            operacion_suma(num1, num2)
        elif (operacion == "resta"):
            operacion_resta(num1, num2)
        elif (operacion == "multiplicacion"):
            operacion_multiplicacion(num1, num2)
        elif (operacion == "division"):
            operacion_division(num1, num2)

while True:
    num1 = (input("Ingrese primer numero"))
    if (num1=="salir"):
        break
    num2 = (input("Ingrese el segundo numero"))            
    if (num2=="salir"):
        break
    calculadora_flexible(num1,num2,["suma", "resta", "multiplicacion", "division"])