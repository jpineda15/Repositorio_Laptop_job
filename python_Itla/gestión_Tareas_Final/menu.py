from funcionAgre import agregarTarea # Del módulo funcionAgre.py importamos la Funcion agregarTarea 
from leerTareas import mostrar_registros # Del módulo leerTareas.py importamos la Funcion mostrar_registros 
from upadateTarea import actualizarTarea # Del módulo upadateTarea.py importamos la Funcion actualizarTarea
from eliminar_Tareas import eliminar_registro # Del módulo eliminar_Tareas.py importamos la Funcion eliminar_registro

# Creamos la Funcion menuInicio
def menuInicio():
    # Lista menu 
    menu = [
        "\n**** --- Gestión de Tareas --- ****\n",
        '1. Agregar Tareas.',
        '2. Consultar Tareas.',
        '3. Actualizar Tareas.',
        '4. Eliminar Tareas.'
    ]
    menu = '\n'.join(menu)
    
    
    while True:
        
        print(f"{menu}")
        
        # Este control de excepciones verifica que la entrada sea un número, de lo contrario muestra un error y solicita nuevamente si no lo es.
        try:
            opción = int(input("\nSelecciona una opción (1-4). Para Salir Ingrese 0: "))
        except ValueError:
            print("\nPor favor ingresa un número válido.")
            continue
        
        
        if opción == 1:
            agregarTarea() # Funcion para agregar Tarea | OK
        elif opción == 2:
            mostrar_registros() # Leer y filtrar tarea almacenada | OK
        elif opción == 3:
            actualizarTarea() # Funcion para actualizar (update) a los registro | OK
        elif opción == 4:
            eliminar_registro() # Funcion para eliminar (delete) a los registro | OK
        elif opción == 0:
            print("Saliendo del programa...")
            return 'Sistema Cerrado..'
            break 
        else:
            print(f"La opción no válida: {opción}. Por favor, selecciona una opción válida.\n")


