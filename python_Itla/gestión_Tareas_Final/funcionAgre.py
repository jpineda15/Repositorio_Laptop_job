from datetime import datetime, timedelta
from opciones import prioridadF, categoríaF
import sqlite3

ruta_db = "PythonGit\python_Itla\gestión_Tareas_Final\database\gestorTarea.db"
# Inicialización de las variables para la conexión y el cursor
my_conexión = None
cursor = None

# Función que crea un Id único con el Año/mes/día/Hora:Minutos
def genera_id():
    tiempoId = datetime.now().strftime('%y%m%d%H%M%S')
    nuevo_id = f'GT-{tiempoId}'
    return nuevo_id


# Agregar Tareas
def agregarTarea():
    
    tareAg = {}
    
    fech_Creada = datetime.now()
    fech_Vence = fech_Creada + timedelta(days=30)
    
    while True:
        
        try:
            numTarea = int(input("\nIndique la cantidad de tareas que desea agregar. Para Salir Ingrese 0: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue
        
        if numTarea > 0: 
            
            for c in range(numTarea):
                
                print("\n ---Agregando Nueva Tarea---")
                
                nom_Tarea = input("\n Título de la Tarea: ").title()
                desc_Tarea = input("\nIngrese una Breve descripción de la Tarea: ").title()
                prio_Tarea = prioridadF()
                cate_Tarea = categoríaF()
                
                tareAg = {
                    '_id': genera_id(),
                    'Título': nom_Tarea,
                    'Descripción': desc_Tarea,
                    'Fecha_Vencimiento': fech_Vence.strftime('%Y-%m-%d %H:%M:%S'),
                    'Prioridad': prio_Tarea, 
                    'Categoría': cate_Tarea, 
                    'Estado': 'Pendiente', 
                    'Fecha_Creación': fech_Creada.strftime('%Y-%m-%d %H:%M:%S')
                }
                
                
                try:
                    my_conexión = sqlite3.connect(ruta_db, timeout=10) # timeout=10 tiempo máximo de espera(en segundo) 
                    cursor = my_conexión.cursor() #Crear un cursor para ejecutar comandos SQL
                    
                    #Preparar los nombres de las columnas y los valores para la inserción
                    columnas = ', '.join(tareAg.keys())
                    signos = ', '.join('?' * len(tareAg))
                    valores = tuple(tareAg.values())
                    
                    #Construcción de la consulta SQL de inserción
                    query = f'''
                        INSERT INTO GESTION ({columnas})
                        VALUES ({signos})
                    '''
                    
                    cursor.execute(query, valores)
                    my_conexión.commit()
                    
                    print(f"Tarea agregada con _id: {tareAg['_id']}")
                    
                    # Contador de registros
                    cursor.execute("SELECT COUNT(*) FROM GESTION")
                    total_registros = cursor.fetchone()[0]
                    print(f"Total de tareas en la base de datos: {total_registros}")
                    
                except Exception as ex:
                    print("Error:", ex)
                finally:
                    if cursor:
                        cursor.close()
                    if my_conexión:
                        my_conexión.close()
            
        elif numTarea == 0:
            print("Saliendo...")
            return "Sistema Cerrado.."
            break
        else:
            print("\nEl número ingresado no es una opción válida. Intenta nuevamente.")
