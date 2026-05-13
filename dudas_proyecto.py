tablero_cpu = [0,0,0,5,5,5,5,5,0,0,2,2,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

tablero_jg1 = []
tablero_cpu = [0,0,0,5,5,5,5,5,0,0,2,2,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#simulando atacar la posicion 4
if tablero_cpu[4] != 0:
    print("Barco encontrado!!")
    print(f"el barco encontrado es el {tablero_cpu[4]}")
    tablero_cpu[4] = "x"
else:
    tablero_cpu[4] = "f"

print(tablero_cpu)

# simulo atacar la posicion 1
if tablero_cpu[1] != 0:
    print("Barco encontrado!!")
    print(f"el barco encontrado es el {tablero_cpu[1]}")
    tablero_cpu[1] = "x"
else:
    print("Fallaste el disparo!!!")
    tablero_cpu[1] = "f"

print(tablero_cpu)

if tablero_cpu[3] != 0:
    print("Barco encontrado!!")
    print(f"el barco encontrado es el {tablero_cpu[4]}")
    tablero_cpu[3] = "x"
else:
    tablero_cpu[3] = "f"

print(tablero_cpu)



#Funcion crear el tablero del cpu (verificar que no chhoquen barcos)
#Funcion crear el tablero del jugador
#Funcion atacar el cpu
#Funcion atacar el jugador
