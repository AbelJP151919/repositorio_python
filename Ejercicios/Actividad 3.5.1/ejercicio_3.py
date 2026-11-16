while True:

    usuario = input("Ingrese su usuario: ")
    if usuario == "":
        print("El usuario no puede quedar vacio. Vuelva a introducir el usuario")
        continue
    contrasena = input("Ingrese su contraseña: ")
    if contrasena == "":
        print("La contraseña no puede quedar vacio. Vuelva a introducir la contraseña")
        continue
    contrasena2 = input("Vuelva a introducir su contraseña: ")

    if contrasena != contrasena2:
        print("Las contraseñas no coinciden. Vuelva a introducir las contraseñas")
        continue
    else:
        print("Usuario Registrado correctamente")
        break



