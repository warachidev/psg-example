# %%
contador_primos = 0
numero = 2
while contador_primos < 20:
    primo = True
    for i in range(2,numero):
        if(numero%i == 0):
            primo=False
            break
    if(primo):
        contador_primos+=1
        print(numero)
    numero+=1