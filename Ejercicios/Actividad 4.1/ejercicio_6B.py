
lista_usuarios = ["JOSE", "PEPE", "JUAN", "CARLOS", "ALEJANDRO"]
lista_contrasena = ["1234", "4321", "abcd", "dcba", "1111"]




usuario = input("Ingrese el usuario: ").upper()
contrasena = input("Ingrese el contrasena: ")


if usuario in lista_usuarios and contrasena in lista_contrasena:
    print("Acceso Permitido")
else:
    print("Acceso Denegado")