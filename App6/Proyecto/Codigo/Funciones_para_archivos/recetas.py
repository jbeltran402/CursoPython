"""clase que efectua dunciones para las recetas"""
import os
from pathlib import Path

class Recetas:
    """Funciones asociadas a la administracion de recetas"""
    ruta_global:str = str(Path('App6','Proyecto','Recetas'))
    
    def numero_de_archivos_en_un_directorio(self) -> int:
        """
        Cuenta el número total de archivos en un directorio y sus subdirectorios.
        
        Returns:
            int: Número total de archivos en el directorio y sus subdirectorios.
        """
        total_archivos:int = 0
        for _, _, archivos in os.walk(str(self.ruta_global)):
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
            listado_de_recetas = recetas.listar_recetas_de_un_directorio(directorio)
            if len(listado_de_recetas) < 1:
                return "sin elementos"
            print("\nIngrese el numero de una receta en la que desea leer:")
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
        ruta:Path = Path(self.ruta_global,directorio)
        for _,_,nombre_de_archivos in os.walk(str(ruta)):
            for archivo in nombre_de_archivos:
                # Si el archivo no es un archivo de zona de identificación y
                # termina con ".txt", lo añadimos a la lista de recetas
                if ".txt:Zone.Identifier" not in archivo:
                    listado_de_recetas.append(archivo.replace(".txt",""))
        return listado_de_recetas
    
    def leer_receta(self, categoria_seleccionada:str, receta_seleccionada:str) -> None:
        """
        Lee y muestra el contenido de una receta seleccionada.

        Args:
            categoria_seleccionada (str): La categoría de la receta seleccionada.
            receta_seleccionada (str): El nombre de la receta seleccionada.

        Returns:
            None
        """
        ruta_receta: Path = Path(self.ruta_global, categoria_seleccionada, receta_seleccionada + '.txt')
        with open(str(ruta_receta), 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
        input("\n\033[1;33mPara volver al menú principal precione Enter\033[0m")
    
    def crear_receta(self, categoria_seleccionada:str) -> None:
        """
        Solicita al usuario el nombre de una categoría, verifica si ya existe (ignorando mayúsculas 
        y minúsculas),y si no existe, crea un nuevo directorio para la categoría.

        Returns:
            None
        """
        nombre_receta = input("Introduce el nombre de la receta que desea crear\n")
        ruta_receta:Path = Path(self.ruta_global,categoria_seleccionada,nombre_receta+'.txt')
        print("Introduce las líneas de texto (deja una línea vacía para terminar):\n")
        while True:
            linea = input()
            if linea == "":
                break
            else:
                with open(ruta_receta, 'a', encoding='utf-8') as archivo:
                    archivo.write(linea + '\n')
        input("\n\033[1;33mPara volver al menú principal precione Enter\033[0m")
    def eliminar_receta(self, categoria_seleccionada:str, receta_seleccionada:str) -> None:
        """
        Elimina una receta seleccionada.

        Args:
            categoria_seleccionada (str): La categoría de la receta seleccionada.
            receta_seleccionada (str): El nombre de la receta seleccionada.

        Returns:
            None
        """
        ruta_receta: Path = Path(self.ruta_global, categoria_seleccionada, receta_seleccionada + '.txt')
        try:
            os.remove(ruta_receta)
            print(f'\nLa receta {receta_seleccionada} fue eliminada correctamente')
        except OSError as error:
            print('\n\033[1;33mError al eliminar el rirectorio '+ error+'\033[0m')
        input("\n\033[1;33mPara volver al menú principal precione Enter\033[0m")
