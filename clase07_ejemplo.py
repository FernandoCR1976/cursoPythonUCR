#Crea un programa que:

# Use un diccionario para guardar nombres de estudiantes y sus notas.
# Permita:

# Agregar estudiantes y notas.
# Mostrar todos los estudiantes con sus notas.
# Calcular el promedio de las notas.


# Indique cuántos estudiantes están aprobados (nota ≥ 70).

def ingresar_estudiantes():
    estudiantes = {}
    cantidad = int(input("Por favor ingrese la cantidad de estudiantes a registrar"))

    for i in range(cantidad):
        print(f"\nEstudiantes {i+1}")
        nombre = input("Nombre: ")
        nota = float(input("Nota: "))
        estudiantes[nombre]=nota
    return estudiantes

# ejemplo_diccionario = {}
# nombre = "Luis"
# nota = 100
# ejemplo_diccionario[nombre] = nota

# print(ejemplo_diccionario)

def mostrar_estudiantes(estudiantes):
    print("\n Lista de estudiantes y sus notas")
    for nombre, nota in estudiantes.items():
        print(nombre,"->" ,nota)

def calcular_promedio(estudiantes):
    suma = 0
    for nota in estudiantes.values():
        # suma = suma + nota
        suma += nota
    promedio = suma / len(estudiantes)
    return promedio

def contar_aprobados(estudiantes):
    aprobados = 0
    for nota in estudiantes.values():
        if nota >= 70:
            aprobados += 1
    return aprobados

def main():
    estudiantes = ingresar_estudiantes()
    mostrar_estudiantes(estudiantes)

    promedio = calcular_promedio(estudiantes)
    aprobados = contar_aprobados(estudiantes)

    print("\n Resultados")
    print("Promedio del grupo: ", promedio)
    print("Cantidad de estudiantes aprobados: ", aprobados)

main()

tablero = ["22","333","444","5555"]
tablero_real = [0,2,2,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,00,0,0,0,0,0,0,00,0,0,0,0,0,0,0,4,4,4,4,0,0,0,0,0,0,0,00,0,0,0,0,0,0,00,0,0,0,0,0,0,00,0,0,0,0,0,0,00,0,0,0,0,0,0,0,5,5,5,5,5]