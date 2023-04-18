# Indices
texto = "Hola Mundo"

# Hola Mundo
# ||||||||||
# 0123456789
Buscar = texto[3]
print(f"\nEl indice 3 Hace referencia a la letra {Buscar}\n")

#  H o l a   M u n d o
#  | | | | | | | | | |
# -0-1-2-3-4-5-6-7-8-9
Buscar = texto[-3]
print(f"El indice -3 Hace referencia a la letra {Buscar}\n")

# Hola Mundo
# ||||||||||
# 0123456789
Buscar = texto.index("n")
print(f"La letra 'n' se encuentra en la posicion {Buscar}\n")

# Hola Mundo
# ||||||||||
# 0123456789
Buscar = texto.index("o",4)
print(f"La letra 'o' a partir de la posicion 4 se encuentra en la posicion {Buscar}\n")

# Para buscal al revez se usa rindex