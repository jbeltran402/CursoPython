# Juego en el que :
# 1).Solo hay 8 intentos para advinar el numero 
# 2).El numero es generado aleatoreamente 
# 3).El rango del numero es del 1 al 100

from random import randint 

numero_aleatorio = randint(1,100)
print(numero_aleatorio)
rango = {"menor":1,"mayor":100}

nombre = input("¿Cúal es tu nombre?\n")

estado = True
for i in range(8):
    while estado:
        if estado:
            numero = int(input(f"{i+1}). Escribe un número entre el {rango['menor']} y el {rango['mayor']}\n ->"))
        if numero > 100 or numero < 1:
            continue
        else:
            estado = False

    if numero == numero_aleatorio:
        print(f"Felicidades {nombre} ¡Haz ganado!")
        break
    elif numero > numero_aleatorio and rango['mayor'] > numero:
        print("El numero seleccionado es mayor que el numero aleatorio")
        rango['mayor'] = numero
        estado = True
    elif numero < numero_aleatorio and rango['menor'] < numero:
        print("El numero seleccionado es menor que el numero aleatorio")
        rango['menor'] = numero
        estado = True
    else:
        print("El numero esta fuera de rango")
        estado = True
print("Fin del juego")