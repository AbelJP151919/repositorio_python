
horas = int(input("Ingrese las horas de la pelicula: "))
minutos = int(input("Ingrese las minutos de la pelicula: "))

if(minutos > 60):
    minutos = minutos - 60
    horas = horas + 1

print("La duracion de la pelicula es: ", horas, "horas y ", minutos, " minutos")