# %%
class SaldoInsuficiente(Exception):
    pass

saldo = 10000.00
while True:
   try:
    monto = float(input("Ingrese el monto que desea retirar: ")) 
    if(monto > 1000.00):
        raise Exception("El monto no puede superar los 1000.00")
    elif(monto > saldo):
        raise SaldoInsuficiente("Saldo Excedido")
    else:
        saldo -= monto
   except SaldoInsuficiente as e:
       print("Error personalizado: ", e)
   except Exception as e:
       print("Error genérico: ",e)
   finally:
       print("Saldo actual: ", saldo)