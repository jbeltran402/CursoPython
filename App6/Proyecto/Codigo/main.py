"""Clase principal"""
import os
from Funciones_para_archivos.recetas import Recetas
from Funciones_para_directorios.categorias import Categorias

recetas = Recetas()
categorias = Categorias()

while True:
    os.system('clear')
    print(f"\nBienvenido al Recetario - {recetas.numero_de_archivos_en_un_directorio()} recetas disponibles")
    print("\nPor favor ingrese el numero de una de las siguientes opciones:")
    print("\n   1. Leer receta")
    print("   2. Crear receta")
    print("   3. Crear categoría")
    print("   4. Eliminar receta")
    print("   5. Eliminar categoría")
    print("   6. Finalizar programa")
    
    opcion_seleccionada = input("\n - ")

    if opcion_seleccionada == "1":
        os.system('clear')
        categoria_seleccionada = categorias.listar_categorias()
        if categoria_seleccionada != 'sin elementos':
            os.system('clear')
            receta_seleccionada = recetas.listar_recetas(categoria_seleccionada)
            if receta_seleccionada != 'sin elementos':
                os.system('clear')
                recetas.leer_receta(categoria_seleccionada, receta_seleccionada)
            else:
                input("\n\033[1;33m No hay recetas en la categoría, presione Enter para volver al menú de opciones\033[0m")
        else:
            input("\n\033[1;33m No hay categorías, presione Enter para volver al menú de opciones\033[0m")
    elif opcion_seleccionada == "2":
        os.system('clear')
        categoria_seleccionada = categorias.listar_categorias()
        if categoria_seleccionada != 'sin elementos':
            os.system('clear')
            recetas.crear_receta(categoria_seleccionada)
        else:
            input("\n\033[1;33m No hay categorías, presione Enter para volver al menú de opciones\033[0m")
    elif opcion_seleccionada == "3":
        os.system('clear')
        categorias.crear_categoria()
    elif opcion_seleccionada == "4":
        os.system('clear')
        categoria_seleccionada = categorias.listar_categorias()
        if categoria_seleccionada != 'sin elementos':
            receta_seleccionada = recetas.listar_recetas(categoria_seleccionada)
            if receta_seleccionada != 'sin elementos':
                recetas.eliminar_receta(categoria_seleccionada, receta_seleccionada)
            else:
                input("\n\033[1;33m No hay recetas en la categoría, presione Enter para volver al menú de opciones\033[0m")
        else:
            input("\n\033[1;33m No hay categorías, presione Enter para volver al menú de opciones\033[0m")
    elif opcion_seleccionada == "5":
        os.system('clear')
        categoria_seleccionada = categorias.listar_categorias()
        if categoria_seleccionada != 'sin elementos':
            categorias.eliminar_categorias(categoria_seleccionada)
        else:
            input("\n\033[1;33m No hay categorías, presione Enter para volver al menú de opciones\033[0m")
    elif opcion_seleccionada == "6":
        break
    else:
        input("\n\033[1;33m Selección incorrecta, presione Enter para reintentar\033[0m")
