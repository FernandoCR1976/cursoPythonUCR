opcion = 0
while opcion != 4:
    print("*****MENU*****")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Has seleccionado la opción 1")
    elif opcion == 2:
        print("Has seleccionado la opción 2")
    elif opcion == 3:
        print("Has seleccionado la opción 3")
    elif opcion == 4:
        print("Saliendo del programa...")   
        break
    else:
        print("Opción no válida")