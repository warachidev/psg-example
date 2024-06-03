# %%
edad_cliente = int(input("Edad del cliente: "))
compra = float(input("Monto: "))

if edad_cliente >= 60 and compra > 1000:
    print("Descuento 10%: -",compra * 0.1)
elif edad_cliente < 18 and compra > 500:
    print("Descuento 5%: -",compra * 0.05)
else:
    print("Descuento 2%: -",compra * 0.02) 