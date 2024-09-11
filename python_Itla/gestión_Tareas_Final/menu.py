from funcionAgre import agregarTarea
from leerTareas import mostrar_registros
from upadateTarea import actualizarTarea

def menuInicio():
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
        
        try:
            opción = int(input("\nSelecciona una opción (1-4). Para Salir Ingrese 0: "))
        except ValueError:
            print("\nPor favor ingresa un número válido.")
            continue
        
        
        if opción == 1:
            agregarTarea() # Funcion para agregar Tarea
        elif opción == 2:
            mostrar_registros() # Leer y filtrar tarea almacenada 
        elif opción == 3:
            actualizarTarea()
        elif opción == 4:
            pass  # Función que consulte el listado de tareas
        elif opción == 5:
            pass  # Función que borre tarea existente
        elif opción == 0:
            print("Saliendo del programa...")
            return 'Sistema Cerrado..'
            break 
        else:
            print(f"La opción no válida: {opción}. Por favor, selecciona una opción válida.\n")


