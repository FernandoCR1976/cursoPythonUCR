# palabra = "Python"

# for letra in palabra:
#     print(letra)            

# print(palabra[0]) # Imprime la primera letra de la palabra (P)

# #hacer un programa que me indique el largo  de la palabra ingresada por el usuario

# palabra_usuario = input("Ingrese una palabra: ")
# largo_palabra = len(palabra_usuario) # La función len() devuelve la cantidad
# print(f'La palabra "{palabra_usuario}" tiene {largo_palabra} letras.')

#Hacer un programa que reciba una palabra y una letra en especial y determine cuántas veces aparece esa letra en la palabra.
palabra_usuario = input("Ingrese una palabra: ")
letra_usuario = input("Ingrese una letra: ")

contador = 0

for letra in palabra_usuario:
    if letra == letra_usuario:
        #contador += 1
        contador = contador + 1 # Otra forma de escribir contador += 1

        "secretarias"
print(f'La letra "{letra_usuario}" aparece {contador} veces en la palabra "{palabra_usuario}".')

#Hacer un programa que valide  si una contraseña ingresada por el usuario es segura. Para esto, la contraseña debe tener al menos 8 caracteres, contener al menos una letra mayúscula, una letra minúscula y un número.
#sera que tenemos que usar varios if ?
#Definir que sucede cuando se cumple o no una condicion 
#determinar una manera para distinguir entre mayusculas, minusculas y numeros
#determinar si es una letra o un numero
#definir una variable para cada condicion y luego evaluar si se cumplen todas las condiciones al final

mensaje_general = "Por favor, ingrese una contraseña que cumpla con los siguientes requisitos:\n- Al menos 8 caracteres\n- Contener al menos una letra mayúscula\n- Contener al menos una letra minúscula\n- Contener al menos un número"
contrasenna = input(mensaje_general)
tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False

if len(contrasenna) >= 8:
    for i in contrasenna:
     if i.isupper():
        tiene_mayuscula = True
     elif i.islower():
        tiene_minuscula = True
     elif i.isdigit():
        tiene_numero = True 

if tiene_mayuscula == True and tiene_minuscula == True and tiene_numero == True:
    print("La contraseña es segura.")

if tiene_mayuscula and tiene_minuscula and tiene_numero:
    print("La contraseña es segura.")
else:    
   print("La contraseña no es segura. Por favor, asegúrese de cumplir con todos los requisitos.")