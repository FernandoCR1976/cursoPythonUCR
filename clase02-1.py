edad = int(input("Ingrese su edad: "))
#Debemos detarminar si un persona es mayor de edad o no.
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ejercicio: Ingresar un número y determinar si es par o impar.
numero = int(input("Ingrese un número: "))  
if numero % 2 == 0:
    print(f'El número {numero} es par.')
else:
    print(f'El número {numero} es impar.')

segundo_numero = int(input("Ingrese otro número: "))
par = True

if segundo_numero % 2 == 0:
    par = True
else:
    par = False

if par == True:
    print(f'El número {segundo_numero} es par.')
else:
    print(f'El número {segundo_numero} es impar.')


# Ejercicio: Una tienda ofrece un descuento del 10% para compras superiores a $100. Ingresar el monto de la compra y mostrar el precio final después de aplicar el descuento si corresponde.

monto_compra = float(input("Ingrese el monto de la compra: "))

if monto_compra > 100:
    descuento = monto_compra * 0.10
    precio_final = monto_compra - descuento
    print(f'El precio final después de aplicar el descuento es: ${precio_final:.2f}') # El formato :.2f se utiliza para mostrar el precio final con dos decimales.
else:   
    print(f'El precio final es: ${monto_compra:.2f}')      


#Ejercicio, en una caseta de peaje se cobra $5 para vehículos livianos y $10 para vehículos pesados. Durante el día, se registran 3 vehículos y se desea calcular el total recaudado al final del día. Ingresar el tipo de vehículo (liviano o pesado) para cada uno de los 3 vehículos y mostrar el total recaudado.
