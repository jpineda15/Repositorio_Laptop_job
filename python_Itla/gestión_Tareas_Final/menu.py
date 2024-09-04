


# Menu 
def menuInicio():
    menu =[
        "Gestión de Tareas:",
        '1. Agregar Tareas.',
        '2. Actualizar Tareas.',
        '3. Consultar Tareas.',
        '4. Eliminar Tareas.',
        '5. Salir de Sistema.'
    ]
    menu = '\n'.join(menu)
    print(f"{menu}")
    
    # Agregar validador de errores por si ingresan str
    
    contador = 0
    contador2 = 0
    intento = 3
    
    while True:
        
        # Control de error si se ingresa un valor no permitido
        try:
            opción = int(input("Selecciona una opción (1-5): "))
        except ValueError:
            contador += 1
            print(f"El valor ingresado no es valida. Tienes {contador} intento de {intento}. Por favor, ingresa un número del 1 al 5.") 
            
            if contador >= intento: # condición para salir del sistema por intento fallido
                print("Has alcanzado el número máximo de intentos. El sistema se cerrará...")
                break
            continue
        
        contador2 += 1
        
        if opción == 1:
            pass #Agregar función que agregue tarea
        elif opción == 2:
            pass #Función que actualice tarea existente
        elif opción == 3:
            pass #Función que Consulte el listado de Tareas
        elif opción == 4:
            pass ##Función que borre tarea existente
        elif opción == 5:
            print("Saliendo del programa...")
            break
        elif contador2 >= intento:
                print(f"Usted tiene {intento} Intento, Ingresando un Valor Incorrecto: {str(opción)}")
                break
        else:
                print(f"La opción no válida: {opción}. Por favor, selecciona una opción válida.\n")

