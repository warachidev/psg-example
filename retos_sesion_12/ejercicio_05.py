#%%
nombre = input("ingrese un nombre: ")
gustos = input("Ingrese sus gustos musicales: ")
gustos_musicales = gustos.split(",")
if nombre:
    print ( "Rock existe dentro de la lista" if 'rock' in gustos_musicales else "Rock no existe dentro de la lista" )
else:
    print("Nombre no válido")
