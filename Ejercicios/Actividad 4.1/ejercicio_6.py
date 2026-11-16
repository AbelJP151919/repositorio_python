

usuario_guardado = "PEPE"
con_guardada = "1234"



usuario = input("Ingrese el usuario: ")
contrasena = input("Ingrese el contrasena: ")

if usuario == usuario_guardado and contrasena == con_guardada:
    print("Acceso Permitido")
else:
    print("Acceso Denegado")