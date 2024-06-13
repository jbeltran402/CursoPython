"""Modulo que captura informacion del sistema."""
import os
from pathlib import Path

class Categorias:
    """Clase que maneja la obtención de categorías de las recetas."""
    ruta_global:str = str(Path('App6','Proyecto','Recetas'))
    
    def listar_categorias(self)-> str:
        """Muestra una lista de categorías y solicita al usuario que elija una.

        Returns:
            str: La categoría seleccionada por el usuario.
        """
        estado = True
        while estado:
            print("\nIngrese el numero de una categoria en la que desea buscar:")
            listado_de_categorias = self.listado_de_categorias()
            for indice, categoria in enumerate(listado_de_categorias):
                print(f"   {indice+1}. {categoria}")
            try:
                categoria_seleccionada = int(input("\n - "))
                if categoria_seleccionada <= len(listado_de_categorias):
                    string_categoria_seleccionada = listado_de_categorias[categoria_seleccionada - 1]
                    return string_categoria_seleccionada
                else:
                    os.system('clear')
                    print("\n\033[1;33mEl valor ingresado no coincide con la lista de categorias\033[0m")
            except ValueError:
                os.system('clear')
                print("\n\033[1;33mEl valor ingresado no coincide con la lista de categorias\033[0m")
                
    def listado_de_categorias(self)-> list:
        """Obtiene una lista de nombres de directorios.

        Returns:
            list: Una lista de nombres de categorías.
        """
        nombres_directorios:list = []
        for _,directorios,_ in os.walk(self.ruta_global):
            for directorio in directorios:
                nombres_directorios.append(directorio)
        return nombres_directorios
    
    def crear_categoria(self) -> None:
        """Solicita un nombre y crea el directorio con este nombre
        """
        while True:
            categoria = input("Escriba el nombre de la categoria que desea crear\n")
            listado_de_categorias: list = self.listado_de_categorias()
            if categoria.lower() in (cat.lower() for cat in listado_de_categorias):
                print ("\n\033[1;33mEl nombre ingresado ya hace parte de una categoria\033[0m\n")
            else :
                os.makedirs(os.path.join(self.ruta_global, categoria))
                print(f"Categoría '{categoria}' creada exitosamente.")
                break
        input("\n\033[1;33mPara volver al menú principal precione Enter\033[0m")