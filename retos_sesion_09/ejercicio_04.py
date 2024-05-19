#%%
productos = ["Pan","Huevo","Leche","Tomate","Lechuga"]
precios = [0.50,0.80,8.50,1.50,2.0]
index_leche = productos.index("Leche")
print("Index Leche", index_leche)
productos.pop(index_leche)
precios.pop(index_leche)
print(productos)
print(precios)

print("Precio del Pan", precios[productos.index("Pan")])
print("Precio del Huevo", precios[productos.index("Huevo")])
print("Producto mas caro ",max(precios))
print("Producto mas barato ",min(precios))

print("Productos en total: ", len(productos))
print("Precio total de los produtos: ", sum(precios))

productos.sort()
precios.sort()
print(productos)
print(precios)

productos.clear()
print(productos)