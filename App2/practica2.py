# Calcular comisiones del 13%
nombre = input("¿Cual es tu nombre?")
ventas = input("¿Cuales fueron tus ventas?")
porcentaje = (float(ventas)*13)/100
print(f"{nombre} el porcentaje por tus ventas es :{round(porcentaje,2)}")