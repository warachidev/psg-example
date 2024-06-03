# %%
comidas = {
    "carne" : {"animales": ["león", "tigre"] },
    "frutas" : {"animales": ["mono", "elefante"]}
    }

print ( comidas )

comidas.update( 
               {"vegetales" : {"animales": ["conejo", "elefante"]}, 
                "hierbas" : {"animales": ["conejo", "siervo"]}, 
                "insectos" : {"animales": ["mono"]}, 
                "nueces" : {"animales": ["mono", "ardilla"]} 
                } )
print ( comidas )

print ( 'carne' in comidas )
# %%
frutas = comidas.pop('frutas')
print ( comidas )