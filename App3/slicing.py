# Slicing Permite extraer fragmentos de un texto

texto = "ABCDEFGHIJKLMNÑOPQRSTVWXYZ"
Fragmento = texto[2:5]
print(Fragmento)

Fragmento = texto[1:10:2]
print(Fragmento)

#Recorrer un texto al revez
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])