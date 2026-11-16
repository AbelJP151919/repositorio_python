try:
    grupo_0 = []
    grupo_1 = []
    grupo_2 = []

    totalGrupo = [
        grupo_0,
        grupo_1,
        grupo_2
    ]

    def introducir_Alumnos():
        nombre_Alumno = input("Introduce el nombre del Alumno: ")
        index_grupo = int(input("Introduce el numero de grupo al que deseas añadir al alumno(0, 1, 2): "))
        lista_grupo = []
        if index_grupo <len(totalGrupo):
            respuesta  = input("Deseas añadir el grupo?(S/N)").upper()

            if respuesta == "S":

                totalGrupo.append(lista_grupo)

                lista_grupo.append(nombre_Alumno)
                respuesta2 = input(f"Quieres añadir el alumno al grupo {index_grupo}: ")
                if respuesta2 == "S":
                    print(f"Añadiendo el alumno: {nombre_Alumno} al el grupo: {index_grupo}")
                    lista_grupo.append(nombre_Alumno)
                elif respuesta2 == "N":
                    print("Saliendo...")
            elif respuesta == "N":
                print("Saliendo...")

        elif lista_grupo in totalGrupo[index_grupo]:
            respuesta3 = input(f"Deseas introducir el alumno {nombre_Alumno} al el grupo {index_grupo}: ")

            if respuesta3 == "S":
                print(f"Añadiendo el alumno: {nombre_Alumno} al el grupo: {index_grupo}")
                totalGrupo[index_grupo].append(nombre_Alumno)
            elif respuesta3 == "N":
                print("Saliendo...")

    introducir_Alumnos()
    print(totalGrupo)

except:
    print("Error en el sistema")


