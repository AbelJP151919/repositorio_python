"""Ejercicio 5 (ejercicio_5.py).
Escribir un programa similar al anterior pero en el que además del número se guardará el nombre,
el dni y si la persona es mayor de edad guardará un 1, en caso contrario un 0.
Se utilizará un menú con las siguientes opciones: 1- Nueva entrada; 2- Consulta; 3- Listado; 0- salir.
En la consulta se indicará si el número ha sido utilizado.
En el listado se mostrará una lista de los asistentes, indicando el mensaje "menor de edad" si el valor guardado es 0.
"""
import time

lista_nombres = []
lista_edades = []
lista_entradas = []
mensaje_menor = "MENOR DE EDAD"

mayor_18 = 1

print("=== SISTEMA DE ENTRADAS ===")

respuesta_programa = 1

while respuesta_programa != 0:
    respuesta_programa = int(input("INTRODUCE UNA DE LAS SIGUIENTES OPCIONES(1. NUEVA ENTRADA-2. CONSULTA-3. LISTADO-0. SALIR): "))
    match respuesta_programa:
        case 1:
            nueva_entrada = int(input("INTRODUCE EL NUMERO DE LA ENTRADA: "))
            if nueva_entrada not in lista_entradas:
                nombre_nuevo = input("INTRODUCE EL NOMBRE DE LA PERSONA: ")
                edad = int(input("INTRODUCE LA EDAD: "))
                if edad >= 18:
                    lista_nombres.append(nombre_nuevo)
                    lista_edades.append(edad)
                    lista_entradas.append(nueva_entrada)

                    print("LA ENTRADA SE HA REGISTRADO CORRECTAMENTE")



                elif edad < 18:
                    lista_nombres.append(nombre_nuevo)
                    mayor_18 = 0
                    if mayor_18 == 0:
                        lista_edades.append((edad, mensaje_menor))
                    lista_entradas.append(nueva_entrada)
                    print("LA ENTRADA SE HA REGISTRADO CORRECTAMENTE")


            elif nueva_entrada in lista_entradas:
                print("LA LISTA YA ESTA REGISTRADA")

        case 2:
            modelo_busqueda = int(input("INTRODUCE EL NUMERO DE TU ENTRADA: "))
            if modelo_busqueda in lista_entradas:
                print("LA ENTRADA YA ESTA EN LA LISTA")

        case 3:
            print("=== LISTADO DE LAS ENTRADAS ===")
            for nombre, edad, entrada in zip(lista_nombres, lista_edades, lista_entradas):
                print(f"NOMBRE: {nombre}, EDAD: {edad}, ENTRADA: {entrada}")

        case 0:
            print("SALIENDO")
            time.sleep(0.5)
            respuesta_programa = 0


