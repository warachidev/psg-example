# %%
habitats = {
    "polo norte" : {"especies": {"oso polar", "morsa", "ballena"} }, 
    "amazonas" : {"especies": {"tigre", "mono", "guacamayo"} }
    }

print (habitats)

habitats.update(africa = {"especies" : {"león", "chita", "zebra"} }, 
                oceania = {"especies" : {"ballena azul", "manatí"} })

print (habitats)

print ('amazonas' in habitats)

habitats["amazonas"]["especies"].add('anaconda')

print ( habitats )

print ( habitats["amazonas"] )