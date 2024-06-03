# %%
arca = {
    "perro" : 2, 
    "gato" : 2, 
    "tigre" : 2, 
    "mono" : 2, 
    "unicornio" : 0, 
    "jirafa" : 1
    }

arca.update(ardilla = 2, cerdo = 2)
print ( arca )

iterador = iter(arca.items())
print ( type(iterador) )
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)

print ('dragon' in arca)

del (arca["unicornio"])
print (arca)

arca.update( jirafa = 2 )
print ( arca )

arca.clear()
print ( arca )