# Reange presenta un enterbalo el cual puede ser manipulado, 
# de diversas maneras, tales como:
#   - Convertir ese intervalo de numeros en un listado 
#   - presentar un listado que puede saltarse sifras 

# Range a lista
mi_lista = list(range(0,21))
print(f"rango de numeros\n- {mi_lista} \n")

# range a lista saltandose los numeros inpares
mi_lista = list(range(2,21,2))
print(f"rango de numeros pares\n- {mi_lista}")
