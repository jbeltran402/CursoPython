# funcion simple
def imprimir_en_pantalla():
    print("Hola mi nombre es juan")

# Funciones usando return
def multiplicar(numero1:int, numero2:int):
    return numero1*numero2

palabra = 'juan'
def invertir_palabra(palabra):
    print(palabra[::-1].upper()) 

lista_numeros = 0
def suma_menores (lista):
    for item in lista:
        if item>0 and item<1000:
            lista_numeros += item
    return lista_numeros

imprimir_en_pantalla()
resultado:int = multiplicar(10,10)
print(resultado)
invertir_palabra('juan')



