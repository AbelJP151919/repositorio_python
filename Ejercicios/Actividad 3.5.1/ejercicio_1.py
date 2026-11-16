respuesta_tarjeta = input("Tienes tarjeta de socio?(Si/No): ")

precio_comida = float(input("Precio de la comida: "))

descuento_cliente = 25/100

respuesta_tarjeta.upper()

if respuesta_tarjeta == "SI" or precio_comida >= 100:
    precioTotal = precio_comida - (descuento_cliente * precio_comida)

    print("CUENTA CLIENTE:")
    print("Precio de la comida: ", precio_comida)
    print("Descuento: ", descuento_cliente * 100)
    print("Precio final: ", precioTotal)

elif respuesta_tarjeta == "NO" or precio_comida <= 100:
    print("CUENTA CLIENTE:")
    print("Precio de la comida: ", precio_comida)


