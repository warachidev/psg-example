# %%
while True:
    n = int(input("Ingrese un numero: "))
    primo = True
    if(n==0):
        break
    for i in range(2, n):
        if (n%i == 0):
            primo = False
            break
    print(n, "Es Primo" if primo else "No es primo")