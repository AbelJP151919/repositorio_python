try:
    contador = 1
    def multiplo_3_for():
        print("Numeros multiplos de 3")
        for i in range(1, 51):

            if i % 3 == 0:
                print(i)
    def multiplo_3_while(contador):
        print("Numeros multiplos de 3 con while")
        while contador >=1 and contador <=50:

            contador+=1
            if contador%3 == 0:
                print(contador)
    multiplo_3_for()
    multiplo_3_while(contador)




except:
    print("Error del servidor")