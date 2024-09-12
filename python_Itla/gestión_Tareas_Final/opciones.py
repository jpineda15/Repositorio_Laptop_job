
# Prioridades de los registros.
def prioridadF():
    tarea_Prio = [
        'Prioridades de las Tareas: ',
        '1. Alta',
        '2. Media',
        '3. Baja',
        '4. Crítica'
    ]
    print('\n','\n'.join(tarea_Prio))
    
    while True:
        try:
            prio = int(input("\nSelecciona una opción (1-4). Para Salir Ingrese 0: "))
        except ValueError:
            print("\nPor favor ingresa un número válido.")
            continue
        
        if prio == 1:
            return 'Alta'
        elif prio == 2:
            return 'Media'
        elif prio == 3:
            return 'Baja'
        elif prio == 4:
            return 'Crítica'
        elif prio == 0:
            print("Saliendo...")
            return "Sistema Cerrado.."
            break
        else:
            print("\nEl número ingresado no es una opción válida. Intenta nuevamente.")

# Característica de los registros.
def categoríaF():
    tarea_Cat = [
        "Característica de las Tareas:",
        '1. Trabajo',
        '2. Personal',
        '3. Urgente',
        '4. Estudios',
        '5. Hogar',
        '6. Finanzas',
        '7. Salud'
    ]
    print('\n','\n'.join(tarea_Cat))
    while True:
        try:
            cate = int(input("\nSelecciona una opción (1-7). Para Salir Ingrese 0: "))
        except ValueError:
            print("\nPor favor ingresa un número válido.")
            continue
        
        if cate == 1:
            return 'Trabajo'
        elif cate == 2:
            return 'Personal'
        elif cate == 3:
            return 'Urgente'
        elif cate == 4:
            return 'Estudios'
        elif cate == 5:
            return 'Hogar'
        elif cate == 6:
            return 'Finanzas'
        elif cate == 7:
            return 'Salud'
        elif cate == 0:
            print("Saliendo...")
            return "Sistema Cerrado.."
            break
        else:
            print("\nEl número ingresado no es una opción válida. Intenta nuevamente.")


# Estado de los registros.
def estadoF():
    tare_Estado = [
        "Estado de las Tareas Registradas",
        '1. En Progreso',
        '2. Completada',
        '3. En Espera',
        '4. Aplazada',
        '5. Cancelada',
        '6. Pendiente'
    ]
    print('\n','\n'.join(tare_Estado))
    while True:
        try:
            statu = int(input("\nSelecciona una opción (1-6). Para Salir Ingrese 0: "))
        except ValueError:
            print("\nPor favor ingresa un número válido.")
            continue
        
        if statu == 1:
            return 'En Progreso'
        elif statu == 2:
            return 'Completada'
        elif statu == 3:
            return 'En Espera'
        elif statu == 4:
            return 'Aplazada'
        elif statu == 5:
            return 'Cancelada'
        elif statu == 6:
            return 'Pendiente'
        elif statu == 0:
            print("Saliendo...")
            return "Sistema Cerrado.."
            break
        else:
            print("\nEl número ingresado no es una opción válida. Intenta nuevamente.")