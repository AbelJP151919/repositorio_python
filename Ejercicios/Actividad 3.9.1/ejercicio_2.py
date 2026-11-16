lista_entradas = [1, 3, 6, 8, 4, 5, 23, 122, 454, 21, 90]

entrada = int(input("Introduzca el numero de su entrada: "))

if entrada in lista_entradas:
    print("No puedes pasar")
else:
    print("Puedes pasar")