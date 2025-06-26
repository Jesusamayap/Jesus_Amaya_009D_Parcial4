
import funcion_4 as u

while True:
    print("\nMENU PRINCIPAL")
    print("1.- ingrese usuario")
    print("2.- buscar usuario")
    print("3.- eliminar usuario")
    print("4.- salir")
    opcion = input("ingrese opcion (1-4): ")

    if opcion == "1":
        u.ingresar_usuario()
    elif opcion == "2":
        u.buscar_usuario()
    elif opcion == "3":
        u.eliminar_usuario()
    elif opcion == "4":
        print("Programa terminado. Gracias por usuarlo.")
        break
    else:
        print("debe seleccionar una opcion valida")
