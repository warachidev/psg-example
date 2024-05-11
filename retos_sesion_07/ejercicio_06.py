#Retorno centrado en una cadena de largo ancho.
# El relleno se realiza utilizando el carácter de relleno especificado 
# (el valor predeterminado es un espacio ASCII). 
# La cadena original se devuelve si el ancho es menor o igual que len(s).

cadena = "Hola"
print (cadena.center(10))
print (cadena.center(10, "+"))

#Devuelve el número de apariciones no superpuestas de la subcadena sub en el rango [inicio, fin]. 
# Los argumentos opcionales de inicio y fin se interpretan como en notación de sector.

#Si sub está vacío, devuelve el número de cadenas vacías entre caracteres, que es la longitud de la cadena más uno.
cadena = "HHHHHHhOOoOooOOola"
print (cadena.count("H"))

#Devuelve Verdadero si la cadena termina con el sufijo especificado; de lo contrario, devuelve Falso. el sufijo también puede ser una tupla de sufijos a buscar. Con inicio opcional, la prueba comienza en esa posición. Con final opcional, deje de comparar en esa posición.
cadena = "123456789"
print (cadena.endswith("9"))
print (cadena.endswith("4", 0, 4))

#Devuelve Verdadero si solo hay espacios en blanco en la cadena y hay al menos un carácter; Falso en caso contrario.
cadena = "A "
print (cadena.isspace())

#Devuelve una copia de la cadena sin los caracteres finales. 
# El argumento chars es una cadena que especifica el conjunto de caracteres que se eliminarán. 
# Si se omite o es Ninguno, el argumento chars por defecto elimina los espacios en blanco.
# El argumento chars no es un sufijo; más bien, se eliminan todas las combinaciones de sus valores:
cadena = "abd---rtytr--rittñ---bbad--"
print (cadena.rstrip("abd-"))