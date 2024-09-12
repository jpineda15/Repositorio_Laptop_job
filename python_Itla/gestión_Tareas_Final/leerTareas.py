from opciones import prioridadF, categoríaF # type: ignore
import sqlite3

# Ruta de la base de datos
ruta_db = "PythonGit/python_Itla/gestión_Tareas_Final/database/gestorTarea.db"

# Inicialización de las variables para la conexión y el cursor
my_conexión = None
cursor = None



def vistaGeneral():
    # Conectar a la base de datos SQLite
    my_conexión = sqlite3.connect(ruta_db, timeout=10)
    my_conexión.row_factory = sqlite3.Row # Acceso a resultados por nombre de columna
    cursor = my_conexión.cursor()
    
    
    # Consulta SQL para obtener los primeros 5 registros de la tabla
    consulta = "SELECT _id, Título, Descripción, Fecha_Vencimiento, Prioridad, Categoría, Estado, Fecha_Creación FROM GESTION LIMIT 5"
    
    try:
        cursor.execute(consulta)
        registros = cursor.fetchall()
        
        # Iterar sobre los resultados y mostrarlos formateados
        for a, ver in enumerate(registros, start=1):
            _id = ver[0] if ver[0] is not None else 'N/A'
            Título = ver[1] if ver[1] is not None else 'N/A'
            Descripción = ver[2] if ver[2] is not None else 'N/A'
            FechaFin = ver[3] if ver[3] is not None else 'N/A'
            Prioridad = ver[4] if ver[4] is not None else 'N/A'
            Categoría = ver[5] if ver[5] is not None else 'N/A'
            Estado = ver[6] if ver[6] is not None else 'N/A'
            FechCrea = ver[7] if ver[7] is not None else 'N/A'
            
            print(f'\nRegistro {a}:')
            print(f'  ID: {_id}')
            print(f'  Título: {Título}')
            print(f'  Descripción: {Descripción}')
            print(f'  Fecha_Vencimiento: {FechaFin}')
            print(f'  Prioridad: {Prioridad}')
            print(f'  Categoría: {Categoría}')
            print(f'  Estado: {Estado}')
            print(f'  Fecha_Creación: {FechCrea}')
            print('-' * 20)
            
        print("\nVista de los 5 primeros Registros.")
    except sqlite3.Error as e:
        print(f"Error al consultar en la base de datos: {e}")
    finally:
        # Cerrar la conexión
        my_conexión.close()



def mostrar_registros():
    
    vistaGeneral()
    
    # Conectar a la base de datos SQLite
    my_conexión = sqlite3.connect(ruta_db, timeout=10)
    my_conexión.row_factory = sqlite3.Row
    cursor = my_conexión.cursor()
    
    while True:
        
        filtro_Tarea = prioridadF()  # Llamamos la función de las Prioridades
        
        if filtro_Tarea == "Sistema Cerrado..":
            break
        
        query = """
        SELECT _id, Título, Descripción, Fecha_Vencimiento, Prioridad
        FROM GESTION
        WHERE Prioridad = ?
        LIMIT 5;
        """
        
        cursor.execute(query, (filtro_Tarea,))
        registros = cursor.fetchall()
        
        if registros:  # Verificamos si hay registros
            for i, registro in enumerate(registros, start=1):  # Iteramos sobre los registros y los enumeramos (enumerate) iniciando en 1
                _id, Título, Descripción, Fecha_de_Vencimiento, Prioridad = registro
                
                # Agrega aquí los campos que deseas mostrar
                print(f'\n Registro {i}:')
                print(f'  ID: {_id}')
                print(f'  Título: {Título}')
                print(f'  Descripción: {Descripción}')
                print(f'  Fecha de Vencimiento: {Fecha_de_Vencimiento}')
                print(f'  Prioridad: {Prioridad}')
                print('-' * 20)  # límite de separación entre cada registro
            
            # Imprimir el total de registros
            print(f"\nTotal de registros encontrados: {len(registros)} con Prioridad: {filtro_Tarea}")
            break  # Salir del bucle si hay registro
        else:
            print(f"\nNo hay tareas con prioridad asignada como: '{filtro_Tarea}'.")
    
    my_conexión.close()




