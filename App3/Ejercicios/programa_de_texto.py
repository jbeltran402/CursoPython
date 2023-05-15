# Capurar un texto y capturar 3 letras

letras = []
texto = input("Ingrese el texto que procesar \n - ")
texto = texto.lower()
estado = True
letras_repetidas = {}

for i in range(3):
    letra = input(f"Ingrese letra {i+1} \n - ")
    while estado:
        if len(letra) == 1:
            letras.append(letra.lower())
            estado = False
        else:
            print("----------------------------- \n"
                  +" Solo una letra, ¡Por favor! "
                  +"\n-----------------------------")
            letra = input(f"Ingrese letra {i+1} \n - ")
    estado = True

print("\nAnalisis del texto\n")

# 1). identificar cuantas veces aprarecen las letras selccionadas
for i in range(len(letras)):
    indice_diccionario = letras[i]
    print(f"la letra {indice_diccionario} se repite {texto.count(letras[i])} veces")

# 2). Cuantas palabras hay en total
print(f"\nEl texto cuenta con {len(texto.split())} palabras\n")

# 3). Primera letra del texto y ultima letra
print(f"La primera letra es: {texto[0:1:]}\n")
print(f"La ultima letra es: {texto[-1]}\n")

# 4). Palabras en orden inverso
palabras = texto.split()
palabras.reverse()
print(f"Las palabras en orden inverso son: {' '.join(palabras)}\n")

# 3). Buscar si se encuentra la palabra Python
if "python" in texto :
    print("El texto cuenta con la palabra python\n")
else :
    print("El texto NO cuenta con la palabra python\n")