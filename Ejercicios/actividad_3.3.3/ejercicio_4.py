iva= 21/100

cantidadProductos = 1
listaproductos = []



print("\033[?25hEMPRESA\033[0m")

nombreEmpresa = input("Introduce el nombre de la empresa: ")
nif = int(input("Introduce el nif de la empresa: "))

print("\033[?25hCLIENTE\033[0m")
nombreCliente = input("Introduce el nombre de la cliente: ")
nifCliente = int(input("Introduce el nif del cliente: "))
descuentoCliente = int(input("Introduce el descuento del cliente: "))


print("\033[?25hPRODUCTOS\033[0m")

while cantidadProductos > 0:
    descripcionProducto = input("Introduce el nombre de la descripcion: ")

    precioProducto = float(input("Introduce el precio del producto: "))
    unidadesProductos = int(input("Introduce las unidades del producto: "))

    precioConIVA = (precioProducto * iva) + precioProducto

    precioConDescuento = precioConIVA - (precioConIVA * (descuentoCliente / 100))

    precioTotal = precioConDescuento * unidadesProductos

    productos = [descripcionProducto, precioTotal, unidadesProductos]
    listaproductos.append(productos)

    respuesta = input("Deseas añadir productos?(si/no): ")

    while respuesta != "si" or respuesta != "no":
        respuesta = input("Deseas añadir productos?(si/no): ")
        if respuesta == "si" or respuesta == "no":
            break

    if respuesta == "si":
        continue

    elif respuesta == "no" :
        precioTotalProductos = sum(prod[1] for prod in listaproductos)
        cantidadProductos = 0
        print(
            "NOMBRE EMPRESA -- NIF EMPRESA -- NOMBRE CLIENTE -- NIF CLIENTE -- DESCUENTO CLIENTE -- PRODUCTOS -- PRECIO TOTAL")
        print(
            nombreEmpresa, "--",
            nif, "--",
            nombreCliente, "--",
            nifCliente, "--",
            descuentoCliente, "--",
            listaproductos, "--",
            precioTotalProductos
        )















