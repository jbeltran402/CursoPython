# Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números primos existentes en el 
# rango que va desde cero hasta ese número incluido, y va a devolver la cantidad 
# de números primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.

argumento = 20;

def es_primo(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
def contar_primos(numero):
    primos = []
    for n in range(2, numero + 1):
        if es_primo(n):
            primos.append(n)
            print(n)

    cantidad_primos = len(primos)
    return cantidad_primos


numero = 20
cantidad = contar_primos(numero)
print(f"Encontrados {cantidad} números primos en el rango de 2 a {numero}.")
