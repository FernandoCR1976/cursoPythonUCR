#Funciones

#Funciones sin parametros sin retorno
def saludar():
    print("Hola, bienvenido a la clase de Python")

saludar()

#Funciones sin parametros con retorno
def obtener_saludo():
    return "Hola, bienvenido a la clase de Python"

mensaje = obtener_saludo()
print(mensaje)
print(obtener_saludo())

def prueba_saludo():
    msg_prueba ="Hola, bienvenido a la clase de Python"
    return msg_prueba

acumulador = 0
def suma_uno():
    global acumulador
    acumulador = acumulador + 1
    return acumulador
print(acumulador)
suma_uno()
print(acumulador)

#Funciones con parametros sin retorno
def saludar_persona(nombre):
    print(f"Hola {nombre}, bienvenido a la clase de Python")        

saludar_persona("Fernando")
saludar_persona("Maria")

#Funciones con parametros con retorno
def obtener_saludo_personalizado(nombre):        
    return f"Hola {nombre}, bienvenido a la clase de Python" 
mensaje_personalizado = obtener_saludo_personalizado("Fernando")
print(mensaje_personalizado)       