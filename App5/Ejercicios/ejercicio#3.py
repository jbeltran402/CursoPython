# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def verificar_duplicidad_del_0(*args):
    for i in range(len(args) - 1):
        if (args[i] == 0 and args[i + 1] == 0):
            return True
    return False

print(verificar_duplicidad_del_0(5,6,1,0,0,9,3,5))
print(verificar_duplicidad_del_0(6,0,5,1,0,3,0,1))