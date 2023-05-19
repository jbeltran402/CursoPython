# Permite combinar 2 listas en una sola, manteniendo el orden de ambas 
# y priorizando el tamaño de la más pequeña.

usuarios = ["juan","luisa","henry","camila"]
edades = [10,15,30,12]

listasUnidas = list(zip(usuarios,edades))
print(listasUnidas)

# 

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

paises_capitales = list(zip(paises,capitales))
for pais,capital in paises_capitales:
    print(f"La capital de {pais} es {capital}")
    
numeros_es = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
numeros_pt = ['um', 'dois', 'três', 'quatro', 'cinco']
numeros_en = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(numeros_es,numeros_pt,numeros_en))
print (numeros)