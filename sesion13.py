# %%
#range(Inicio(por defecto 0 e Inclusivo), Fin(Exclisivo), Paso(por defecto 1))

#rango negativo
#range(10, 0, -1)
print(list(range(10,0,-1)))
# %%
for i in [1,2,3,4]:
    print(i)
# %%
print ("Ejemplo 1")
suma =0
for i in range(1,10,2):
    suma+=i
print(suma)
# %%
print ("Ejemplo 2")
for i in range(0, 6):
    print(" "*(5-i) + "*"*i*2+"*")

# %%
print ("Ejemplo 3")
for i in range(1, 11):
    print(i**2, end=" ")

# %%
print ("Ejemplo 4")
pares = []
for i in range(0, 11, 2):
    pares.append(i)
print(pares)
print(type(pares))

# %%
print ("Ejercicio 1")
for i in range(1, 11):
    print(i**3, end=" ")
# %%
for fruta in ['🍎','🍌','🍇','🍉']:
    print(fruta)
# %%
print ("Ejemplo 5")
fiesta = ['🎄','🎆','🎁','🎊','✨','🧨']
for objeto in fiesta:
    print(objeto)
# %%
print ("Ejemplo 6")
frutas =  ('🍅','🍇','🍈','🍉','🍊')
for fruta in frutas:
    print(fruta, end=", ")
# %%
print ("Ejemplo 7")
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
for clave in frutas:
    print(clave, frutas[clave])
# %%
print ("Ejemplo 8")
ciclo_vida = '🥚🐣🐥🐤🐔🍗'
for etapa in ciclo_vida:
    print(etapa, end="->")
# %%
print ("Ejemplo 9")
animales = ['🐶','🐱','🐰','🐭']
for animal in animales:
    print(animal)
# %%
print ("Ejemplo 11")
animales = ['🐶','🐱','🐰','🐭']
for i, animal in enumerate(animales):
    print(i, animal, animales[i])
# %%
print ("Ejercicio 2")
esferas = '⚽🏀🏐🎱'
for i, esfera in enumerate(esferas):
    print(esfera*(i+1))
# %%
print ("Ejemplo 12")
i = 0
while i <= 5:
    print(i)
    i += 1
# %%
print ("Ejemplo 13")
suma = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número: "))
print(suma)
# %%
print ("Ejercicio 3")
numero = int(input("Ingrese un número: "))
while numero >= 0:
    print(numero)
    numero -= 1
# %%
frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta)
print ("Fin")
# %%
frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i)
print ("Fin")
# %%
print ("Ejemplo 15")
contador = 0
while True:
    print(contador)
    contador += 1
# %%
print ("Ejemplo 16")
while True:
    texto = input("Ingrese un texto: ")
    if texto == 'salir':
        break
    print(texto.upper())
print ("Fin")
# %%
print ("Ejercicio 4")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print ("Par" if numero % 2 == 0 else "Impar")
# %%
print ("Ejemplo 17")
pares = [i for i in range(2, 11, 2)]
print(pares)
# %%
print ("Ejemplo 18")
pares = [i for i in range(2, 11) if i % 2 == 0]
print(pares)
# %%
print ("Ejemplo 19")
pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
print(pares)
# %%
print ("Ejercicio 5")
impares = tuple(i for i in range(1, 11) if i % 2 != 0)
print(impares)
# %%
print ("Ejemplo 20")
for i in range(1, 3):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# %%
print ("Ejemplo 21")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print(f"Tabla del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
print ("Fin")
# %%
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
# %%
print ("Ejemplo 22")
n = int(input("Ingrese un número: "))
matriz = [['X' for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)
# %%
n = int(input("Ingrese un numero: "))
matriz = [[(j,i) for i in range(n)] for j in range(j)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)
# %%
