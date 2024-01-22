from pathlib import Path

# Usando el la funcion de path se logra convertir los
# parametros en una ruta relativa, como lo es
# 'Hola','Mi','Nombre' -> Hola/Mi/Nombre

parametros = Path('Hola','Mi','Nombre')
print(parametros)

