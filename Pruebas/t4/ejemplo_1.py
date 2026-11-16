def calcula(a):
    
    resultado = 10/a
    return resultado


try:
    calcula(0)
    print("El numero es igual a 0")

except Exception as e:
    print("El numero no puede ser 0")