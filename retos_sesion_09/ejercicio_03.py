#%%
nombres = ["Alejandro","Marisol","Jhon","Alexa","Monica","Gerardo","Marlene","Jessica","Jorge","Ariel",]
#Obtener una sub lista de 2 a 7
sublista = nombres[1:7]
print(sublista)

#Buscar si existe el nombre "Jhon" en la lista original
valor = "Jhon"
print (valor, nombres.count(valor))

#Ordenar la sub lista alfabéticamente
sublista.sort()
print(sublista)

#Ordenar la lista original alfabéticamente de forma descendente
nombres.sort(reverse=True)
print(nombres)
# %%
