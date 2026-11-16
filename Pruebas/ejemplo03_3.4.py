import math

radio = [5, 10, 15, 20]




def areaCirculo(radio):

    areaTotal = 0

    for r in radio:
        area = math.pi * r ** 2
        areaTotal = areaTotal + area

    print(areaTotal)


def perimetroCirculo(radio):

    perimetroTotal = 0

    for r in radio:
        perimetro = math.pi * r * 2
        perimetroTotal = perimetroTotal + perimetro

    print(perimetroTotal)


areaCirculo(radio)
perimetroCirculo(radio)
