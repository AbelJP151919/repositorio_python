# Definición de monedas como tuplas (valor, nombre)
Euro = (1.12, "Euros")
Yen = (0.0063, "Yens")
Pesos = (0.055, "Pesos")
Bolivares = (0.0011, "Bolivares")

# Lista de monedas
listaMonedas = [Euro, Yen, Pesos, Bolivares]

# Pedir nombre de moneda
nombreMoneda = input("Ingrese el nombre de la moneda: ").strip()

# Buscar la moneda en la lista
for valor, nombre in listaMonedas:
    if nombreMoneda.lower() == nombre.lower():  # Comparación sin importar mayúsculas
        simbolo = input("Ingrese el símbolo de la moneda: ").strip()

        monedaUtilizada = {
            "nombreMoneda": nombre,
            "simbolo": simbolo,
            "valor_moneda": valor
        }

        print("✅ Moneda encontrada:", monedaUtilizada)
        break
else:
    print("❌ Moneda no encontrada en la lista.")




