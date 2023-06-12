nombre = input("Cual es tu nombre? ")
ventas = int(input("¿Cuales son tus ventas? "))
porcentaje = round(ventas * 13 / 100, 2)
print(f"Enhorabuena {nombre} tu comisión por tus ventas son:  ${porcentaje}")

