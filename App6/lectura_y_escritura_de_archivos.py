# r -> Lectura del documento
# W -> Sobrescribir el documento
# a -> Escribe texto al final del documento
archivo =  open('App6/Archivos/MiArchivo.txt','r')

linea2 = archivo.readlines()
print(linea2[1])
archivo.close()

# Creacion de logs
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('App6/Archivos/MiArchivo.txt','a')
for item in registro_ultima_sesion:
    archivo.writelines(item + "\t")
archivo.close()

archivo = open('registro.txt','r')
print(archivo.read())
archivo.close()


# Una forma mas eficiente de realizar la operacion es usando with

def registro_error(nombre_archivo):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write("se ha registrado un error de ejecución")

# de esta manera 'with' se encarga de abrir y cerrar el archivo 