try:
    grupos_totales = []

    respuesta_1 = input("Quieres Añadir a un Alumno a un Grupo?(S/N): ").upper()


    while respuesta_1 != "N":
        nombre_alumno = input("Introduce el nombre del Alumno: ")

        respuesta_2 = input(f"Deseas añadir el alumno {nombre_alumno}?(S/N): ").upper()

        if respuesta_2 == "S":

            nombre_grupo  = input("Introduce el nombre del Grupo al que deseas añadir al alumno: ")

            if nombre_grupo not in grupos_totales:
                grupos_totales.append(nombre_grupo)
                grupos_totales.append([nombre_alumno])
                print(f"Alumno {nombre_alumno} añadido al grupo {nombre_grupo}.")
            elif nombre_grupo in grupos_totales:
                indice_grupo = grupos_totales.index(nombre_grupo)
                grupos_totales[indice_grupo + 1].append(nombre_alumno)
                print(f"Alumno {nombre_alumno} añadido al grupo existente {nombre_grupo}.")

        elif respuesta_2 == "N":
            print("Saliendo...")
            respuesta_1 = "N"



        if respuesta_1 == "S":
            respuesta_1 = input("\n¿Quieres añadir a OTRO Alumno al sistema?(S/N): ").upper()

        elif respuesta_1 == "N":
            print("Saliendo...")
            print(f"Grupos Totales: {grupos_totales}")


except:
    print("Error en el servidor")
