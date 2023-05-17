# Permite generarun contador sin declarar una variable en cero; 
# se crea directamente en la iteración.

lista = ["a","s","d","f","g","h","j"]

for index,item in enumerate(lista):
    print(index,item)


# Este ejemplo Busca el indice en el que se encuentra la palabra que inicia con una M 

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index,item in enumerate(lista_nombres):
    if item[0] == "M":
        print(index)