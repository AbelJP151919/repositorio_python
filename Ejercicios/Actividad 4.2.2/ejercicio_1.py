try:

    contador = 9
    contador2 = 21
    def menor_mayor():
        print(f"Numeros del 10 al 20")

        for i in range(9, 20):
            i+=1
            print(f"{i}")

    def mayor_menor():
        print(f"Numeros del 20 al 10:")
        for i in reversed(range(9, 20)):
            i+=1

            print(f"{i}")

    def menor_mayor_con_while(contador):
        print(f"Numeros del 10 al 20 con while")
        while contador >= 9 and contador <= 19:
            contador+=1
            print(f"{contador}")

    def mayor_menor_con_while(contador2):
        print(f"Numeros del 20 al 10 con while:")
        while contador2 <= 21 and contador2 > 10:

            contador2-=1
            print(f"{contador2}")

    menor_mayor_con_while(contador)
    mayor_menor_con_while(contador2)
except:
    print("Error del servidor")




