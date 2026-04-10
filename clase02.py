# numero_cualquiera = 15

# #es_par = numero_cualquiera % 2 == 0 # El operador == se utiliza para comparar.
# residuo = numero_cualquiera % 2
# es_par = residuo == 0
# es_impar = residuo != 0
# print(f'El número {numero_cualquiera} es par: {es_par}')
# print(f'El residuo de {numero_cualquiera} dividido entre 2 es: {residuo}')
# print(f'El número {numero_cualquiera} es impar: {es_impar}')

# # Operadores de comparación
# # Igualdad: ==
# # Desigualdad: !=
# # Mayor que: >
# # Menor que: <
# # Mayor o igual que: >=
# # Menor o igual que: <=

# cancelacion = "SI"
# estado = cancelacion == "SI"
# print(f'La cancelación es: {estado}')

# score = 85
# aprobado = score >= 60
# print(f'El cliente aprobó: {aprobado}')

# lista_de_numeros = [1, 2, 0.50, 4, 5]

# # Ingresando valores a una variable
# edad = input("Ingrese su edad: ")
# print(f'La edad ingresada es: {edad}')

# #Ejercicio: Ingresar el nombre de una persona y mostrar un mensaje de bienvenida personalizado.
# nombre_usuario = input("Ingrese su nombre: ")
# print(f'¡Bienvenido, {nombre_usuario}! Esperamos que tengas un excelente día.')

#Ejercicio: Ingresar dos números y mostrar su suma, resta, multiplicación y división.... y el promedio de los dos números.
primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))   

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
division = primer_numero / segundo_numero
promedio = (suma) / 2


print(f'La suma de {primer_numero} y {segundo_numero} es: {suma}')
print(f'La resta de {primer_numero} y {segundo_numero} es: {resta}')
print(f'La multiplicación de {primer_numero} y {segundo_numero} es: {multiplicacion}')
print(f'La división de {primer_numero} y {segundo_numero} es: {division}')
print(f'El promedio de {primer_numero} y {segundo_numero} es: {promedio}')
