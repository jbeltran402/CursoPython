lista = ["a","b","c"]
lista2 = ["d","e","f"]
print(lista[1])

lista[1] = "juan"
print(lista+lista2)

lista.append("d")
print(lista)

lista.pop()
print(lista)

lista.pop(1)
print(lista)

# .sort() sobre escribe la lisa y la ordena
Lista_desordenada = ["f","e","d","c","b","a"]
Lista_desordenada.sort()
print(Lista_desordenada)

Lista_desordenada.reverse()
print(Lista_desordenada)
