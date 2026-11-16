
nombre = input("Introduce el nombre: ")
lista_nombres = []
respuesta = "S"
while respuesta != "N":
    respuesta = input("Quieres introducir otro nombre?(S/N)").upper()
    if respuesta == "S":
        nombre = input("Introduce otro nombre: ")
    lista_nombres.append(nombre)

print(lista_nombres)