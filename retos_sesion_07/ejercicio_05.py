cadena = input ("Ingresa una cadena de texto: ")
cadena_lower = cadena.lower()
cadena_sin_espacio = cadena_lower.replace(" ","")
print ( cadena_sin_espacio == cadena_sin_espacio[::-1])