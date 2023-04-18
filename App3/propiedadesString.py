# Los String son inmutables, lo que se puede cambiar en la variable 

# Los estring se pueden multioplicar
texto = "ja"
print(texto * 10)

# Para qe hayan saltos de linea sin usar \n se uan """
texto = """Hola mi nombre es Juan
Y me gusta programar en Python,
Es muy útil"""
print(texto)
print("Hola" in texto)
print("perro" not in texto)
print(len(texto))
