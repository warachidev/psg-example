# %%
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
animales = dict(tupla)
print ( animales )
aves = animales.pop('aves')
print ( aves )
print ( animales )
animales.update({'gato':'🐈'})
print( animales )
animales['perros'] = animales['perro']
print ( animales )
animales['perros'] = ['🐶','🐕']
print ( animales )
del animales['perro']
print ( animales )

# %%
