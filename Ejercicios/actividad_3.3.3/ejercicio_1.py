
cantidad = int(input("Introduce una cantidad de euros: "))


resto = cantidad % 500
billete500 = resto // 200

resto = cantidad % 200
billete200 = resto // 100

resto = cantidad % 100
billete100 = resto // 50

resto = cantidad % 50
billete50 = resto // 20

resto = cantidad % 20
billete20 = resto // 10

resto = cantidad % 10
billete10 = resto // 5

resto = cantidad % 5
billete5 = resto // 2

resto = cantidad % 2
billete2 = resto // 1

resto = cantidad % 1
billete1 = resto // 0.5

resto = float(cantidad % 0.5)
billete50cent = resto // 0.20

resto = float(cantidad % 0.20)
billete20cent = resto // 0.10
resto = float(cantidad % 0.10)
billete10cent = resto // 0.05
resto = float(cantidad % 0.05)
billete5cent = resto // 0.02
resto = float(cantidad % 0.02)
billete2cent = resto // 0.01
resto = float(cantidad % 0.01)
billete1cent = resto // 0.01


print("500 euros: ", billete500)
print("200 euros: ", billete200)
print("100 euros: ", billete100)
print("50 euros: ", billete50)
print("20 euros: ", billete20)
print("10 euros: ", billete10)
print("5 euros: ", billete5)
print("2 euros: ", billete2)
print("1 euro: ", billete1)
print("50 centimos: ", billete50cent)
print("20 centimos: ", billete20cent)
print("10 centimos: ", billete10cent)
print("5 centimos: ", billete5cent)
print("2 centimos: ", billete2cent)
print("1 centimo: ",billete1cent)


