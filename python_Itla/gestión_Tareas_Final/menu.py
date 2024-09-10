from funcionAgre import solicitar_input, agregarTarea
from leerTareas import mostrar_registros
from upadateTarea import actualizarTarea

def menuInicio():
    menu = [
        "\n**** --- Gestión de Tareas --- ****\n",
        '1. Agregar Tareas.',
        '2. Consultar Tareas.',
        '3. Actualizar Tareas.',
        '5. Eliminar Tareas.',
        '6. Salir de Sistema.'
    ]
    menu = '\n'.join(menu)
    
    
    while True:
        print(f"{menu}")
        opción = solicitar_input("\n Selecciona una opción (1-5) :" , int)
        
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
        elif opción == 6:
            print("Saliendo del programa...")
            break
        elif opción is None:
            pass
        else:
            print(f"La opción no válida: {opción}. Por favor, selecciona una opción válida.\n")

#menuInicio()
