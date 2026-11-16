
radio = 5
PI = 3.1415926
def areaCirculo(radio):
    global PI
    area = PI * radio ** 2
    print(area)

def perimetroCirculo(radio):
    global PI
    perimetro = PI * radio * 2
    print(perimetro)


areaCirculo(radio)
perimetroCirculo(radio)
