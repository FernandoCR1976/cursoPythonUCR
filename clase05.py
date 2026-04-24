# palabra = "manzana"
# for letra in palabra:
#     print(letra)

# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     print(numero)   

#for i in range(5):
    #print(i)

#Necesito  imprimir en pantalla los numeros del 1 al 10, sin que el 0 aparezca
acumulador = 10
for i in range(10): # Hace que el bloque de código se repita la cantidad de veces que yo deseo
    acumulador -= 1
    print(acumulador)

for i in range(1, 11): # Hace que el bloque de código se repita la cantidad de veces que yo deseo
    print(i)

for i in range(1, 11, 2): # Hace que el bloque de código se repita la cantidad de veces que yo deseo
    print(i)

for i in range(10, 0, -1): # Hace que el bloque de código se repita la cantidad de veces que yo deseo
    print(i)

for i in range(20,10,-2): # Hace que el bloque de código se repita la cantidad de veces que yo deseo
    print(i)

for i in range(15,20): # Hace que el bloque de código se repita la cantidad de veces que yo deseo
    print(i)    


contador = 0
while contador < 11:
    print(contador)
    contador += 1
    