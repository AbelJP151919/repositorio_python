try:
    dinero = float(input("Ingrese el numero total de dinero: "))

    descuento = 0

    if dinero < 100:
        print("No tienes descuento")
        print(f"Dinero: {dinero}")
    elif dinero >= 100 and dinero <= 499:
        descuento = 5 / 100
        print(f"Descuento: {descuento * 100}%")
        print(f"Dinero: {dinero - (dinero * descuento)}")
    elif dinero >= 500 and dinero <= 999:
        descuento = 10 / 100
        print(f"Descuento: {descuento * 100}%")
        print(f"Dinero: {dinero - (dinero * descuento)}")
    elif dinero >= 1000:
        descuento = 15 / 100
        print(f"Descuento: {descuento * 100}%")
        print(f"Dinero: {dinero - (dinero * descuento)}")
except:
    print("Error en el servidor")
