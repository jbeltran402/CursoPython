# Variable
entero = 1

# identificar el tipo de dato con type
print(entero)
print(type(entero))

# Sobrecargar variable a Float 
entero = 0.24
print(entero)
print(type(entero))

# Convertir Entre tipos
string = input("¿Cual es tu edad? ")
entero = int(string)
entero = entero + 1
print(entero)
print(type(entero))

# Formatear cadena de texto
# A).
string = input("¿Cual es tu edad? ")
entero = int(string)
entero = entero + 1
print(f"{entero} -> Numero entero")
print(type(entero))

# B
string = input("¿Cual es tu edad? ")
entero = int(string)
entero = entero + 1
print("{} Numero entero".format(entero))
print(type(entero))