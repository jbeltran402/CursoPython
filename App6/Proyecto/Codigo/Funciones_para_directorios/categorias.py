"""Modulo que captura informacion del sistema."""
import os

class Categorias:
    """Clase que maneja la obtención de categorías de las recetas."""

    def listar_categorias(self)-> str:
        """Muestra una lista de categorías y solicita al usuario que elija una.

        Returns:
            str: La categoría seleccionada por el usuario.
        """
        categorias = Categorias()
        estado = True
        while estado:
            print("\nIngrese el numero de una categoria en la que desea buscar:")
            listado_de_categorias = categorias.numero_de_categorias()
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
                
    def numero_de_categorias(self)-> list:
        """Obtiene una lista de nombres de directorios.

        Returns:
            list: Una lista de nombres de categorías.
        """
        nombres_directorios:list = []
        for _,directorios,_ in os.walk('App6/Proyecto/Recetas'):
            for directorio in directorios:
                nombres_directorios.append(directorio)
        return nombres_directorios