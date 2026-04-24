#Hora de jugar !!!! Crea un programa que simule un juego de adivinanza. Para esto va a mostrar en pantalla 6 palabras y el usuario debe de adivinar cual es la palabra correcta... Vas a tener que usar la libreria random para que haga una seleccion aleatoria de la palabra correcta. El programa debe de mostrar un mensaje de felicitaciones si el usuario adivina la palabra correcta o un mensaje de ánimo si no lo hace.    



import random

# Lista de palabras
palabras = ["manzana", "banana", "naranja", "pera", "uva", "fresa"]

# Mezclamos la lista (opcional, solo para que cambie el orden)
random.shuffle(palabras)

# Elegimos una palabra secreta al azar
palabra_secreta = random.choice(palabras)

# Mostramos las opciones al usuario
print("🎯 Juego de adivinanza")
print("Adivina cuál es la palabra secreta")
print("Opciones:")

for palabra in palabras:
    print("-", palabra)

# Pedimos la respuesta al usuario
respuesta = input("Escribe tu respuesta: ")

# Verificamos si acertó
if respuesta == palabra_secreta:
    print("🎉 ¡Felicitaciones! Adivinaste la palabra correcta.")
else:
    print("😢 No es correcto, pero no te rindas.")
    print("La palabra correcta era:", palabra_secreta)
