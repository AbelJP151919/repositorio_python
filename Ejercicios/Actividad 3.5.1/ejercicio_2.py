precio_articulo = float(input("Ingrese el valor del precio del articulo: "))

n_unidades = int(input("Introduzca el numero de unidades:"))

total_descuento = 0

precio_total = precio_articulo * n_unidades

if precio_total >= 50 and precio_total <= 100:
    total_descuento = 5/100
    precio_con_descuento = precio_total -(precio_total * total_descuento)

    print("FACTURA ARTICULOS:")
    print("Precio Total: ", precio_total)
    print("Precio Con Descuento: ", precio_con_descuento)

elif precio_total > 100 and precio_total < 200:
    total_descuento = 10 / 100
    precio_con_descuento = precio_total - (precio_total * total_descuento)

    print("FACTURA ARTICULOS:")
    print("Precio Total: ", precio_total)
    print("Precio Con Descuento: ", precio_con_descuento)

elif precio_total >= 200:
    total_descuento = 15 / 100
    precio_con_descuento = precio_total - (precio_total * total_descuento)

    print("FACTURA ARTICULOS:")
    print("Precio Total: ", precio_total)
    print("Precio Con Descuento: ", precio_con_descuento)






