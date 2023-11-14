from Dibujo import figura
from random import randint

lista_de_palabras = ["Casa", "Perro", "Gato", "Flor", "Montaña", "Sol", "Agua", "Libro", "Amigo", "Feliz",
                    "Triste", "Jardín", "Amarillo", "Viaje", "Playa", "Árbol", "Canción", "Chocolate", "Estrella", 
                    "Coche", "Sueño", "Invierno", "Verano", "Otoño", "Primavera", "Cielo", "Mar", "Luna", "Calle", 
                    "Ciudad", "Corazón", "Nube", "Comida", "Felicidad", "Tierra", "Aire", "Luz", "Sombra", "Reloj", 
                    "Puente", "Puerta", "Ventana", "Camino", "Espejo", "Bolsa", "Río", "Silencio", "Color", "Arte", 
                    "Palabra"]

def juego_en_pantalla(palabra):

    letras_correctas = ""
    letras_incorrectas = ""
    estado = True
    input_letra = ""

    while (estado):
        
        Letras_en_pantalla = ""
        input_letra = validaciones_de_letra(letras_incorrectas, letras_correctas)
        
        if input_letra in palabra:
            letras_correctas += input_letra
        else:
            letras_incorrectas += input_letra

        if len(letras_incorrectas) >= 6:
            print(figura(len(letras_incorrectas) + 1))
            print (palabra)
            estado = False
            break
        print(figura(len(letras_incorrectas) + 1))

        for letra in palabra:
            hubo_letra_correcta = False
            for letra_correcta in letras_correctas:
                if (letra_correcta == letra):
                    Letras_en_pantalla += letra_correcta+" "
                    hubo_letra_correcta = True
                    break
            if not hubo_letra_correcta:
                Letras_en_pantalla += "_ "    
        print(Letras_en_pantalla)
        
        if len(letras_correctas) == len(palabra):
            print("¡Ganaste!")

    print("Fin del juego")                    

def validaciones_de_letra(letras_incorrectas, letras_correctas):
    while True:
        input_letra = input("Escriba una letra: ").lower()
        if len(input_letra) == 1 and not input_letra.isdigit() and input_letra not in letras_incorrectas and input_letra not in letras_correctas:
            return input_letra
        else:
            print("¡Caracter no válido! Intente nuevamente")


indice_palabra = randint(0, len(lista_de_palabras) - 1)
juego_en_pantalla(lista_de_palabras[indice_palabra].lower())