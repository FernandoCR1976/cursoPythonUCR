#Hacer un programa que reciba el lado de un cuadrado y calcule su area y perimetro. El programa debe de mostrar el resultado en pantalla. Para esto se deben de crear dos funciones, una para calcular el area y otra para calcular el perimetro. Ambas funciones deben de recibir el lado del cuadrado como parametro y retornar el resultado. El programa debe de pedir al usuario que ingrese el lado del cuadrado y luego mostrar el area y el perimetro calculados por las funciones.

def ingreso_lado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    return lado

def calcular_area(l):
    area = l * l
    return area

def calcular_perimetro(l):
    perimetro = 4 * l
    return perimetro


def ejecutar_calculos():
    lado_cuadrado = ingreso_lado()
    area_cuadrado = calcular_area(lado_cuadrado)
    perimetro_cuadrado = calcular_perimetro(lado_cuadrado)
    print(f"El area del cuadrado es: {area_cuadrado}")
    print(f"El perimetro del cuadrado es: {perimetro_cuadrado}")

#ejecutar_calculos()

#Hacer un programa que reciba el radio de un circulo y calcule su area y perimetro. El programa debe de mostrar el resultado en pantalla. Para esto se deben de crear dos funciones, una para calcular el area y otra para calcular el perimetro. Ambas funciones deben de recibir el radio del circulo como parametro y retornar el resultado. El programa debe de pedir al usuario que ingrese el radio del circulo y luego mostrar el area y el perimetro calculados por las funciones.

#Hacer un programa que reciba las notas de un estudiante y calcule su promedio. El programa debe de pedir la cantidad de notas que se van a ingresar, luego debe de pedir al usuario que ingrese cada una de las notas y almacenarlas en una lista. Luego se debe de crear una funcion que reciba la lista de notas como parametro y calcule el promedio, retornando el resultado. Finalmente, el programa debe de mostrar el promedio calculado por la funcion.

def cantidad_notas():
    cantidad = int(input("Ingrese la cantidad de notas: "))
    return cantidad

def ingreso_notas(cantidad):
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def ejecutar_calculo_promedio():
    cantidad = cantidad_notas()
    notas = ingreso_notas(cantidad)
    promedio = calcular_promedio(notas)
    print(f"El promedio de las notas es: {promedio}")

ejecutar_calculo_promedio()
