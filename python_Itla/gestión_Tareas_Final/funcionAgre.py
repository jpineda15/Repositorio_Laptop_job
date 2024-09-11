from datetime import datetime, timedelta # Importamos la clase datetime & timedelta
from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor
from opciones import prioridadF, categoríaF # type: ignore
import sqlite3

try:
    my_conexion = sqlite3.connect("database/gestiorTarea")
except Exception as ex:
    print(ex)

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017') # Conectar al servidor de MongoDB
db = client['Gestión_de_Tareas'] # Seleccionar la base de datos
dbTabla = db['TablaGESTION'] # Seleccionar la colección(Tabla)



# Función que crea un Id unció con la Año/mes/dia/Hora:Minutos
def genera_id():
    tiempoId = datetime.now().strftime('%y%m%d%H%M')
    nuevo_id = f'GT-{tiempoId}'
    return nuevo_id


# Agregar Tareas
def agregarTarea():
    
    tareAg = {}
    
    fech_Creada = datetime.now() # Obtenemos la Fecha de Creación de la tarea
    fech_Vence = fech_Creada + timedelta(days=30) # Obtenemos la Fecha en la que se vence la tarea (OJO realizar condición que cambie a estado terminado si se cumple esta fecha)
    
    while True:
        
        try:
            numTarea = int(input("\nIndique la cantidad de tareas que desea agregar. Para Salir Ingrese 0: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue
        
        if numTarea > 0: 
            
            for c in range(0, numTarea): # iterar la variable iniciando en 0 
                
                print("\n ---Agregando Nueva Tareas---")
                
                nom_Tarea = input("\n Título de la Tarea: ").lower() # Ingresar titulo de la tarea
                
                desc_Tarea = input("\nIngrese una Breve descripción de la Tarea: ").lower() # Ingresar una descripción de la tarea
                
                prio_Tarea = prioridadF() # Llamos la funcion de las Prioridades
                
                cate_Tarea = categoríaF() # Llamos la fucion de las Característica
                
                
                tareAg = {
                    '_id' : genera_id(),
                    'Título': nom_Tarea,
                    'Descripción': desc_Tarea,
                    'Fecha_Vencimiento': fech_Vence.strftime('%Y-%m-%d %H:%M:%S'),
                    'Prioridad': prio_Tarea, 
                    'Categoría': cate_Tarea, 
                    'Estado': 'Pendiente', 
                    'Fecha_Creación': fech_Creada.strftime('%Y-%m-%d %H:%M:%S')
                } 
                
                try: # Se maneja cualquier error que pueda surgir en el proceso de insertar el Id 
                    dbTabla.insert_one(tareAg)
                    print(f'\nDocumento insertado con ID específico: {tareAg["_id"]}')
                except Exception as e:
                    print(f'\nError al insertar documento: {e}')
            
        elif numTarea == 0:
            print("Saliendo...")
            return "Sistema Cerrado.."
            break
        else:
            print("\nEl número ingresado no es una opción válida. Intenta nuevamente.")



"""
1- id_contador: Variable global que se usa para asignar un ID único a cada tarea.
2- global id_contador: Se declara dentro de la función para modificar la variable global.
3- tareAg[id_contador]: Utiliza id_contador como clave en el diccionario para asegurar que cada tarea tenga un ID único.
4- id_contador += 1: Incrementa el contador después de agregar una tarea.
"""

"""
    datetime -->Esta clase se utiliza para manejar fechas y horas. Proporciona métodos para obtener la fecha y hora actual.
    timedelta -->Esta clase representa una duración o diferencia entre dos fechas o tiempos. Se utiliza para realizar operaciones aritméticas con fechas y horas, como sumar o restar días, horas, minutos, segundos, etc., a un objeto datetime.
"""