notasEstudiante = [5, 6, 3, 8, 2]
aprobado = True

notaMediaEstudiante = sum(notasEstudiante) / len(notasEstudiante)

if notaMediaEstudiante >= 5:
    print(notaMediaEstudiante, "aprobado")
    aprobado = True
else:
    print(notaMediaEstudiante, "No aprobado")
    aprobado = False




