#Tupla
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(tupla[0]) #Acceder al primer elemento

#Dicionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(persona)

print(persona["edad"])
persona["edad"] = 31 #Modificar el valor de la edad
persona["profesion"] = "Ingeniero" #Agregar una nueva clave-valor
print(persona)

del persona["profesion"]
print(persona)

persona.pop("ciudad") #Eliminar la clave "ciudad"
print(persona)

productos = {
    "manzana": 500,
    "banana": 50,
    "naranja": 100
}
print(productos)

for producto in productos:
    print(producto) #Imprime el producto y su precio

for precio in productos.values():
    print(precio) #Imprime solo los precios

for producto, precio in productos.items():
    print(f"Producto: {producto}: Precio: ${precio}") #Imprime el producto y su precio


