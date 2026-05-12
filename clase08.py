#Introduccion a POO
class Estudiante:
    def __init__(self,id,nombre,fecha_nacimiento,genero,edad,correo):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.edad = edad
        self.correo = correo

    def to_string(self):
        print(f"Nombre: {self.nombre}  Edad: {self.edad} años  correo: {self.correo}")


estudiante_1 = Estudiante(1234,"Luis Fernando","02/05/1976","Masculino",50,"fernandocorralesm76@gmail.com")
print(estudiante_1.nombre)
estudiante_1.to_string()

#Creen dos estudiantes mas y muestren la informacion de los mismos
estudiante_2 = Estudiante(4567,"Jose Guillermo", "21/11/2007","Masculino", 18,"jose@sindominio.com")
estudiante_3 = Estudiante(8901,"Alba Isabel","14/04/2007","Mujer",19,"isa@sindominio.com")

estudiante_2.to_string()
estudiante_3.to_string()