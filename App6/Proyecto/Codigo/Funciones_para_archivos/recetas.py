"""Modulo que captura informacion del sistema."""
import os

class Recetas:
    """Funciones asociadas a la administracion de recetas"""

    def numero_de_archivos_en_un_directorio(self) -> int:
        """
        Cuenta el número total de archivos en un directorio y sus subdirectorios.
        
        Returns:
            int: Número total de archivos en el directorio y sus subdirectorios.
        """
        total_archivos:int = 0
        for _, _, archivos in os.walk('App6/Proyecto/Recetas'):
            total_archivos += len(archivos)
        return total_archivos
    
    def listar_recetas(self, directorio:str)-> str:
        """Muestra una lista de categorías y solicita al usuario que elija una.

        Returns:
            str: La categoría seleccionada por el usuario.
        """
        recetas = Recetas()
        estado = True
        while estado:
            print("\nIngrese el numero de una receta en la que desea leer:")
            listado_de_recetas = recetas.listar_recetas_de_un_directorio(directorio)
            for indice, receta in enumerate(listado_de_recetas):
                print(f"   {indice+1}. {receta}")
            try:
                receta_seleccionada = int(input("\n - "))
                if receta_seleccionada <= len(listado_de_recetas):
                    string_receta_seleccionada = listado_de_recetas[receta_seleccionada - 1]
                    return string_receta_seleccionada
                else:
                    os.system('clear')
                    print("\n\033[1;33mEl valor ingresado no coincide con la lista de recetas\033[0m")
            except ValueError:
                os.system('clear')
                print("\n\033[1;33mEl valor ingresado no coincide con la lista de recetas\033[0m")

    def listar_recetas_de_un_directorio(self, directorio:str ) -> list:
        """Devuelve una lista de recetas en un directorio específico.

        Args:
            directorio (str): El nombre del directorio del que se listarán las recetas.

        Returns:
            list: Una lista de nombres de recetas en el directorio especificado.
        """
        listado_de_recetas:list = []
        for _,_,nombre_de_archivos in os.walk(f"App6/Proyecto/Recetas/{directorio}"):
            for archivo in nombre_de_archivos:
                # Si el archivo no es un archivo de zona de identificación y termina con ".txt", lo añadimos a la lista de recetas
                if ".txt:Zone.Identifier" not in archivo:
                    listado_de_recetas.append(archivo.replace(".txt",""))
        return listado_de_recetas