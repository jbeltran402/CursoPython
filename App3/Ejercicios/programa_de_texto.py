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

# 1). identificar cuantas veces aprarecen las letras selccionadas
for i in range(len(letras)):
    indice_diccionario = letras[i]
    letras_repetidas[indice_diccionario] = texto.count(letras[i])

# 2). Cuantas palabras hay en total
print(len(texto.split()))

# 3). Cuantas palabras hay en total

