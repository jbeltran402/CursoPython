"""Modulo que captura informacion del sistema."""
import os

class Recetas:
    """Funciones asociadas a la administracion de recetas"""

    def numero_de_archivos_en_un_directorio(self, ruta:str) -> int:
        """
        Cuenta el número total de archivos en un directorio y sus subdirectorios.

        Args:
            ruta_directorio (str): Ruta del directorio que se va a verificar.

        Returns:
            int: Número total de archivos en el directorio y sus subdirectorios.
        """
        
        total_archivos:int = 0
        for directorio_actual, subdirectorios, archivos in os.walk(ruta):
            total_archivos += len(archivos)
        return total_archivos