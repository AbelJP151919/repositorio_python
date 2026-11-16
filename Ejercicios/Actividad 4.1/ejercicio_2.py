try:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))

    if numero1 > numero2:
        print("El numero ", numero1, " es mayor que ", numero2)
    else:
        print("El numero ", numero2, " es mayor que ", numero1)
except Exception as e:
    print(e)