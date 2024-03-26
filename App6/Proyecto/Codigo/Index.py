recetas = 0
estado_del_menu_principal = True

while estado_del_menu_principal:
    print(f"\nBienvenido al Recetario - {recetas} recetas disponibles")
    print("\nPor favor ingrese el numero de una de las siguientes opciones:")
    print("\n   1. Leer receta")
    print("   2. Crear receta")
    print("   3. Crear categoría")
    print("   4. Eliminar receta")
    print("   5. Eliminar categoría")
    print("   6. Finalizar programa")
    
    opcion_seleccionada = input("\n - ")
    
    if opcion_seleccionada == "1":
        print(opcion_seleccionada)
    elif opcion_seleccionada == "2":
        print(opcion_seleccionada)
    elif opcion_seleccionada == "3":
        print(opcion_seleccionada)
    elif opcion_seleccionada == "4":
        print(opcion_seleccionada)
    elif opcion_seleccionada == "5":
        print(opcion_seleccionada)
    else:
        estado_del_menu_principal = False
    