# %%
class NoFruta(Exception):
    pass

frutas_validas = ["🍅","🍇","🍈","🍉","🍊","🍌","🍍","🍑"]
frutas = []
while True:
    try:
        fruta_nueva = input("Ingresar una fruta")
        if (fruta_nueva == "salir"): break
        if(fruta_nueva in frutas_validas):
            frutas.append(fruta_nueva)
        else:
            raise NoFruta("La fruta no esta en la lista de frutas validas")
    except NoFruta as e:
        print("🚫 NoFruta:", e)  
    except Exception as e:
        print("Error: ", e) 
    finally:
        print(frutas)