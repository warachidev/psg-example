#XNOR Una puerta tiene dos interruptores que controlan dos luces la puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están encendidas, caso contrario la puerta no se abre, ¿qué operador lógico se puede utilizar?
print (not((True or True) and not (True and True)))
print (not((True or False) and not (True and False)))
print (not((False or True) and not (False and True)))
print (not((False or False) and not (False and False)))