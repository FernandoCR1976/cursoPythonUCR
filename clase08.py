#Introduccion a POO
class Estudiante:
    def __init__(self,id,nombre,fecha_nacimiento,genero,edad,correo):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.edad = edad
        self.correo = correo
        self.notas = [] #Atributo para almacenar las notas del estudiante


    def to_string(self):
        print(f"Nombre: {self.nombre}  Edad: {self.edad} años  correo: {self.correo}")

    def agregar_notas(self, nota):
        self.notas.append(nota)

    def mostrar_notas(self):
        contador = 1
        for nota in self.notas:
            
            print(f"Nota {contador}: {nota}")
            contador += 1

    def calcular_promedio(self):
        promedio = sum(self.notas)/ len(self.notas)
        print(f"El estudiante {self.nombre} obtuvo un promedio de: {promedio:.2f}\n")

estudiantes = []

#Creando una FUNCION para agregar estudiantes 

def agregar_estudiante():
    id = int(input("Ingrese la identificacion del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
    genero = input("Ingrese el genero del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    correo = input("Ingrese el correo del estudiante: ")

    estudiante_tmp = Estudiante(id,nombre,fecha_nacimiento,genero, edad, correo)
    
    estudiantes.append(estudiante_tmp)

    print("\nEstudiante Agregado Correctamente\n")

def agregar_notas():
    id_busqueda = int(input("Ingrese el ID del estudiante: "))

    for est in estudiantes:
        if est.id == id_busqueda:
            nota = float(input("Ingrese la nota: "))
            est.agregar_notas(nota)
            print("\nNota agregada correctamente\n")
            return
    print("Estudiante no encontrado")

def mostrar_estudiante():
    id_busqueda = int(input("Ingrese el ID del estudiante: "))
    for est in estudiantes:
        if est.id == id_busqueda:
            est.to_string()
            #est.mostrar_notas()
            #est.calcular_promedio()
            #Se debe de validar si el estudiante tiene notas para mostrar el promedio

def mostrar_todos_estudiantes():

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados\n")
        return
    for est in estudiantes:
        print(f"Nombre: {est.nombre}")
        est.mostrar_notas()
        est.calcular_promedio()
        print("-"*30)
        print(" ")


def menu():
    while True:
        print("------MENU------")
        print("1. Agregar estudiante")
        print("2. Agregar notas")
        print("3. Mostrar estudiante")
        print("4. Mostrar todos")
        print("5. Salir")

        opcion = input("Seleccione una opcion:\n")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_notas()
        elif opcion == "3":
            mostrar_estudiante()
        elif opcion == "4":
            mostrar_todos_estudiantes()
        elif opcion == "5":
            print("\nGracias por utilizar nuestro programa!!!\n")
            print("Saliendo del programa ...")
            break
        else:
            print("Opcion invalida\n")


menu()