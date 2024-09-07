from funcionAgre import solicitar_input, agregarTarea
#import funcionAgre

def menuInicio():
    menu = [
        "\n**** --- Gestión de Tareas --- ****\n",
        '1. Agregar Tareas.',
        '2. Actualizar Tareas.',
        '3. Consultar Tareas.',
        '4. Eliminar Tareas.',
        '5. Salir de Sistema.'
    ]
    menu = '\n'.join(menu)
    
    
    while True:
        print(f"{menu}")
        opción = solicitar_input("\n Selecciona una opción (1-5): ", int)
        
        if opción == 1:
            agregarTarea() # Funcion para agregar Tarea
        elif opción == 2:
            pass  # Función que actualice tarea existente
        elif opción == 3:
            pass  # Función que consulte el listado de tareas
        elif opción == 4:
            pass  # Función que borre tarea existente
        elif opción == 5:
            print("Saliendo del programa...")
            break
        elif opción is None:
            pass
        else:
            print(f"La opción no válida: {opción}. Por favor, selecciona una opción válida.\n")

#menuInicio()
