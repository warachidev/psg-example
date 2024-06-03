# %%
animales = { 
            'mono_arania': 
                { 'nombre_cientifico': 'Arteles geoffroyii', 
                 'clase':'Mammalia', 
                 'orden': 'Primate', 
                 'familia': 'Cebidae', 
                 'alimentacion': ( 'frutas', 'nueces', 'semillas', 'yemas', 'flores', 'hojas', 'insectos arácnidos', 'huevos'), 
                 'habitat': 'Bosques tropicales',
                 'cuidadores_asignados': ('Lic. Juan Carlos Bodoque', 'Luis Merito Pollo', 'Miranda Clivelan Ortega')
                 } }
print ( animales.get('mono_arania') )
alimentos_mono = animales.get('mono_arania').get('alimentacion')
print ( alimentos_mono )
cuidadores = animales.get('mono_arania').get('cuidadores_asignados')
print ( cuidadores )
# %%
