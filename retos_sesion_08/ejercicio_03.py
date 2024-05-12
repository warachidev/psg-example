#%%

cadena = input ("Ingrese una cadena de texto: ")
tupla_1 = tuple(cadena)
tupla = ('!',)
tupla_concatenada = tupla + tupla_1 + tupla
print ( tupla_concatenada)
print ( type(tupla_concatenada))
tupla_triple = tupla_concatenada * 3
print ( tupla_triple)
print ( type(tupla_triple))

# %%
