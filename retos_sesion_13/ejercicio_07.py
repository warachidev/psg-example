# %%
secuencia = []
for i in range (1,101):
    valor = ""
    if (i%3 == 0):
        valor+="Fizz"
    if (i%5 == 0):
        valor+="Buzz"
    if(valor==""):
        secuencia.append(i)
    else:
        secuencia.append(valor)
print(secuencia)