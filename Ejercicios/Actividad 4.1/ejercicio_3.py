try:
    numero1 = int(input("Ingrese el primer numero: "))

    numero2 = int(input("Ingrese el segundo numero: "))

    if numero1 // numero2:
        print("El numero ", numero1, " es multiplo que ", numero2)

except Exception as e:
    print(e)