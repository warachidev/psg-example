#%%
def crear_tablero():
  return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
  for fila in tablero:
    print(" | ".join(fila))

def verificar_jugada(tablero, fila, columna, simbolo):
  if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
    return True
  else:
    return False

def realizar_jugada(tablero, fila, columna, simbolo):
  tablero[fila][columna] = simbolo

def verificar_ganador(tablero, simbolo):
  # Comprobar filas
  for fila in tablero:
    if fila[0] == fila[1] == fila[2] == simbolo:
      return True
  # Comprobar columnas
  for i in range(3):
    if tablero[0][i] == tablero[1][i] == tablero[2][i] == simbolo:
      return True
  # Comprobar diagonales
  if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
    return True
  if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
    return True
  return False

def tablero_lleno(tablero):
  for fila in tablero:
    for casilla in fila:
      if casilla == " ":
        return False
  return True

tablero = crear_tablero()
jugador_actual = "X"

while True:
    mostrar_tablero(tablero)

    # Obtener la jugada del jugador actual
    fila = (input("Ingrese la fila (0, 1 o 2): "))
    if (fila == "salir"): break
    columna = (input("Ingrese la columna (0, 1 o 2): "))
    if (columna == "salir"): break

    # Verificar si la jugada es válida
    while not verificar_jugada(tablero, int(fila), int(columna), jugador_actual):
      print("Jugada inválida. Intenta de nuevo.")
      fila = (input("Ingrese la fila (0, 1 o 2): "))
      if (fila == "salir"): break
      columna = (input("Ingrese la columna (0, 1 o 2): "))
      if (columna == "salir"): break

    # Realizar la jugada
    realizar_jugada(tablero, int(fila), int(columna), jugador_actual)

    # Comprobar si hay un ganador
    if verificar_ganador(tablero, jugador_actual):
      mostrar_tablero(tablero)
      print(f"¡{jugador_actual} gana!")
      break

    # Comprobar si el tablero está lleno
    if tablero_lleno(tablero):
      mostrar_tablero(tablero)
      print("Empate!")
      break

    # Cambiar de jugador
    if jugador_actual == "X":
      jugador_actual = "O"
    else:
      jugador_actual = "X"
# %%
