# - Son elementos unicos (NO se le puede agregar elementos duplicados)
# - NO usan indices
# - Solo se le puede anexar un argumento, por esa razon, se enciarran los 
# parametros con: () o {} o []

mi_set = set([1,2,3,4,5])
print(type(mi_set))

set_2 = {1,2,3}
print(type(set_2))

print(2 in mi_set)
print(10 in mi_set)

# - Se pueden unificar 2 Set y a su vez elimina los valores que se encuentran 
# repetidos
set_3 = {1,2,3}
set_4 = {5,3,2,1,9}
union_sets = set_3.union(set_4)
print(union_sets)

union_sets.add(10)
print(union_sets)

# POP elimina un elemento al azar
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.pop())
print(sorteo)