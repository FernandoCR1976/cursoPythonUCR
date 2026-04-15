color = "rojo"
color = "azul"




palabras = ["hola", "mundo", "python"]




lista_mixta = [1, "hola", 3.14, True]

print(lista_mixta[2])
print(lista_mixta[-1])

lista_mixta[-1] = False # Modificamos el último elemento de la lista
print(lista_mixta[-1])

numeros = [1, 2, 3, 4, 5]
print(numeros)

numeros.append(6) # Agrega el número 6 al final de la lista
print(numeros)

numeros.insert(1,1.5) # Inserta el número 1.5 en la posición 1 (entre el 1 y el 2)
print(numeros)

numeros.remove(5) # Elimina el número 5 de la lista. Si hay varias ocurrencias de 5, solo se eliminará la primera.
print(numeros)

numeros.pop() # Elimina el último elemento de la lista (en este caso, el número 6) y lo devuelve.
print(numeros)

ultimo_elemento = numeros.pop() # Elimina el último elemento de la lista (en este caso, el número 4) y lo devuelve.
print(numeros)  

numeros.clear() # Elimina todos los elementos de la lista, dejándola vacía.
print(numeros)

nueva_lista = [1|0, 20, 30, 40, 50]
cantidad_elementos = len(nueva_lista) # Devuelve la cantidad de elementos en la lista.
print(cantidad_elementos)
print(len(nueva_lista)) # Otra forma de obtener la cantidad de elementos en la lista.

nueva_lista.append(10)
print(nueva_lista)
print(nueva_lista.count(10)) # Devuelve la cantidad de veces que el número 10 aparece en la lista.

for numero in nueva_lista:
    print(numero)

print("Fin del bucle for.")

for i in nueva_lista:
    print(i)


frutas = ["manzana", "banana", "naranja", "pera"]
for fruta in frutas:
    print(fruta)

print("Fin del bucle for.")

valores = [10, 20, 30, 40, 50]

notas = [7.5, 8.0, 9.0, 6.5, 10.0]
suma_notas = 0
vueltas = 0
for i in notas:
    suma_notas = suma_notas + i
    vueltas += 1 # Otra forma de escribir vueltas = vueltas + 1
    #vueltas = vueltas + 1 # Otra forma de escribir vueltas += 1
    print(f'Esta es la vuelta {vueltas} y la suma acumulada es: {suma_notas}')

#EJERCICIO Crea un programa que solicite al usuario ingresar 5 números, los almacene en una lista y luego calcule e imprima la suma de esos números. Ademas debe determinar el promedio de los números ingresados.

secuencia_numeros = ["primer número", "segundo número", "tercer número", "cuarto número", "quinto número"]
numeros_ingresados = []

for i in secuencia_numeros:
    numero = float(input(f'Ingrese el {i}: '))
    numeros_ingresados.append(numero)

suma_numeros = 0

for numero in numeros_ingresados:
    suma_numeros += numero
promedio = suma_numeros / len(numeros_ingresados)
print(f'La suma de los números ingresados es: {suma_numeros}')
print(f'El promedio de los números ingresados es: {promedio}')