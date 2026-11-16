try:
    nota = float(input("Ingrese su nota: "))

    if nota < 5:
        print("Suspenso")
    elif nota >= 5 and nota <=6.9:
        print("Aprobado")
    elif nota >= 7 and nota <=8.9:
        print("Notable")
    elif nota >= 9 and nota <=10:
        print("Sobresaliente")
except Exception as e:
    print(e)