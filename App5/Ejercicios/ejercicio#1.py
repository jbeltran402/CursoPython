# Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
# Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio

def devolver_distintos(parametro_1, parametro_2, parametro_3):
    suma = parametro_1 + parametro_2 + parametro_3;
    if(suma > 15):
        return max(parametro_1,parametro_2,parametro_3)
    elif(suma < 10):
        return min(parametro_1,parametro_2,parametro_3)
    elif(suma >= 10 and suma <= 15):
        return suma - min(parametro_1,parametro_2,parametro_3) - max(parametro_1,parametro_2,parametro_3)

print(f"numero menor {devolver_distintos(5, 3, 1)}")
print(f"numero meyor {devolver_distintos(7, 8, 6)}")    
print(f"numero intermedio {devolver_distintos(2, 2, 7)}")