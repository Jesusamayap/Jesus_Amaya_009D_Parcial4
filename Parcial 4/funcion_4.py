usuarios = {} 

def ingresar_usuario():
    nombre = input("ingrese nombre de usuario: ")
    if nombre in usuarios:
        print("el usuario ya existe")
    else:
        sexo = input("Ingrese sexo: M=Masculino y F=Femenino (M/F): ")
        while sexo != "M" and sexo != "F":
            print("debe ingresar M o F solamente, intente de nuevo.")
            sexo = input("ingrese sexo: M=Masculino y F=Femenino (M/F): ")

        contrasena = input("ingrese contraseña: ")
        while len(contrasena) < 8 or " " in contrasena:
            print("contraseña no válida, debe tener al menos ocho (8) caracteres y no tener espacios en blanco")
            contrasena = input("ingrese contraseña: ")

        usuarios[nombre] = [sexo, contrasena]
        print("contraseña válida.")
        print("usuario ingresado con exito")


def buscar_usuario():
    nombre = input("ingrese nombre de usuario a buscar: ")
    if nombre in usuarios:
        print("Sexo:", usuarios[nombre][0])
        print("Contraseña:", usuarios[nombre][1])
    else:
        print("el usuario no se encuentra")

def eliminar_usuario():
    nombre = input("ingrese nombre de usuario que desea eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("usuario eliminado!")
    else:
        print("no se pudo eliminar el usuario")