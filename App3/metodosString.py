# convertir en mayuscula
texto = "Hola mi nombre es Juan David"

resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split()
print(resultado)

texto_unido=" ".join(["Hola","Mundo","Python"])
print(texto_unido)

# Find arroja el index
resultado = texto.find("Juan")
print(resultado)

# Si Find no encuentra, arroja el -1
resultado = texto.find("juan")
print(resultado)

resultado = texto.replace("Juan","Carlos")
print(resultado)
