from random import *

aleatorio = randint(1,10)
print(f"Numero aleatorio {aleatorio}")

aleatorio = round(uniform(1,3),1)
print(f"Numero aleatorio decimal {aleatorio}")

aleatorio = random()
print(f"Numero aleatorio decimal entre 0 y 1 {aleatorio}")

letras = ["a","b","c","d","e","f","g","h"]
aleatorio = choice(letras)
print(f"letra aleatoria de la a - h -> {aleatorio}")

shuffle(letras)
print(f"letras mezcladas aleatoriamente de la a - h \n{letras}")