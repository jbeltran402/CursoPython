# - las tuplas no pueden ser reasignadas (Su valior es fijo)
    # ocupan menos espacio de memoria
    # Son a prueba de daños
# - Pueden contener cualquier tipo de dato contenido
# - se maneja igual que en los disccionarios o listas

mi_tupla = (1,2,3,4,5)
print(type(mi_tupla))

print(f"Tupla en la posicion -2 es: {mi_tupla[-2]}")

# se puede encadenar una tupla a un conjunto de variables
a,b,c,d,e = mi_tupla
print(a)
print(a,b)
print(f"{a} {b} {c} .......")