# *args
# permite que las funciones acepten indeterminadonumero de argumentos

def sumatoria(*args):
    total = 0
    for item in args:
        total += item
    return total

print(sumatoria(10, 20, 20))

# **kwargs
# Permite anexar un numero indefinido de argumentos a un diccionario

def suma(**kwargs):
    print(kwargs)

suma(a=1,b=2,c=3)

# Capturar el value del diccionario
def lista_atributos(**kwargs):
    return list(kwargs.values())
