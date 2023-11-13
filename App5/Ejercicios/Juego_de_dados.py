from random import randrange

def lanzar_dados():
    dado1 = randrange(1,7)
    dado2 = randrange(1,7)
    return [dado1, dado2]

def evaluar_jugada():
    dados = lanzar_dados()
    suma_dados = dados[0] + dados[1]
    if  suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif  suma_dados > 6 and suma_dados < 10 :
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif  suma_dados >= 10 :
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
print(evaluar_jugada())