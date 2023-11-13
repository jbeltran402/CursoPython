# from collections import OrderedDict

# lista_numeros = []

# def reducir_lista(lista_numeros):
#     lista_numeros_no_repetidos = list(OrderedDict.fromkeys(lista_numeros))
#     return lista_numeros_no_repetidos

def reducir_lista(lista_numeros):
    sin_duplicados = list(set(lista_numeros))
    
    if sin_duplicados:
        numero_alto = max(sin_duplicados)  # Usar max() para encontrar el valor máximo
        sin_duplicados.remove(numero_alto)  # Usar remove() para eliminar el valor máximo
    
    return sin_duplicados

def promedio(lista_numeros):
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros)
    
    return promedio

# Ejemplo de uso:
lista_numeros = [1,2,15,7,2]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)

print("Lista reducida:", lista_reducida)
print("Promedio de la lista reducida:", resultado_promedio)