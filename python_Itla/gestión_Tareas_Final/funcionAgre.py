from datetime import datetime, timedelta # Importamos la clase datetime & timedelta

from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor


# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017') # Conectar al servidor de MongoDB
db = client['Gestión_de_Tareas'] # Seleccionar la base de datos
dbTabla = db['TablaGESTION'] # Seleccionar la colección(Tabla)


# Función para control de error al ingresar valores por teclado
def solicitar_input(mensaje, tipo_dato): # mensaje --> Muestra el mensaje del input | tipo_dato --> recibe el valor ingresado
    contador =0
    intentos = 3
    
    while contador < intentos:
        try:
            valor = tipo_dato(input(mensaje))
            return valor
        except ValueError:
            contador += 1
            print(f"\n El valor ingresado no es válido. Te quedan {intentos - contador} intento(s). Por favor, ingresa un valor correcto.")
        #break
        #print("Has alcanzado el número máximo de intentos. El sistema se cerrará...")
        
        if contador == intentos:
            print("\n Has alcanzado el número máximo de intentos. El sistema se cerrará...")
            return None
            break


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
        # llamamos la función solicitar_input y solicitar el ingreso de la cantidad de tarea a crear.
        numTarea = solicitar_input("\n Indique la Cantidad de Tarea desea Agregar: ", int) 
        
        
        if numTarea is not None and numTarea > 0: # Validamos que el valor ingresado sea mayor a 0 y que sea un valor none.
            
            for c in range(0, numTarea): # iterar la variable iniciando en 0 (OjO)
                
                print("---Agregando Nueva Tareas---")
                nom_Tarea = input("Título de la Tarea: ").lower() # Ingresar titulo de la tarea
                
                if nom_Tarea in tareAg: # si se cumple obviara todo lo siguiente y iniciara nuevamente el bucle for ( OJO ahi que buscar como hacer consulta en la tabla)
                    print(f"La tarea '{nom_Tarea}' ya existe")
                    continue 
                
                desc_Tarea = input("Ingrese una Breve descripción de la Tarea: ").lower() # Ingresar una descripción de la tarea
                
                prio_Tarea = [
                    'Prioridades de las Tareas: ',
                    '1. Alta', #Tareas críticas que deben ser atendidas inmediatamente.
                    '2. Media', #Tareas importantes, pero que no requieren atención inmediata.
                    '3. Baja', #Tareas que pueden esperar o que no tienen una urgencia particular.
                    '4. Crítica' #Tareas que son absolutamente esenciales y que, si no se completan, pueden tener un impacto significativo en el proyecto o negocio.
                ]
                print('\n'.join(prio_Tarea)) # formateamos la salida de la lista 
                prio_Tarea = solicitar_input("Selecciona una opción (1-3): ",int) # Menu de Prioridad
                if prio_Tarea == 1:
                    prio_Tarea = "Alta"
                elif prio_Tarea == 2:
                    prio_Tarea = "Media"
                elif prio_Tarea == 3:
                    prio_Tarea = 'Baja'
                elif prio_Tarea == 4:
                    prio_Tarea = 'Crítica'
                elif prio_Tarea is None:
                    pass
                else:
                    print(f"El numero {prio_Tarea} no es una opción, por favor Selecciona una opción (1-3): ")
                
                
                cate_Tarea =[
                    "Característica de las Tareas: ",
                    '1. Trabajo', #Tareas relacionadas con el empleo, proyectos laborales, reuniones, etc.
                    '2. Personal', #Actividades personales como citas médicas, eventos familiares, o autocuidado. 
                    '3. Urgente', #Tareas que requieren atención inmediata o de alta prioridad.
                    '4. Estudios', #Tareas relacionadas con la educación, como exámenes, deberes o proyectos académicos.
                    '5. Hogar', #Actividades relacionadas con el mantenimiento del hogar, como limpieza, reparaciones o compras domésticas.
                    '6. Finanzas' #Tareas relacionadas con la gestión de dinero, pagos, presupuestos, etc.
                ]
                print('\n'.join(cate_Tarea))# formateamos la salida de la lista
                cate_Tarea = solicitar_input("Selecciona una opción (1-6): ",int) # Menu de Categoría
                if cate_Tarea == 1:
                    cate_Tarea = "Trabajo"
                elif cate_Tarea == 2:
                    cate_Tarea = 'Personal'
                elif cate_Tarea == 3:
                    cate_Tarea = 'Urgente'
                elif cate_Tarea == 4:
                    cate_Tarea = 'Estudios'
                elif cate_Tarea == 5:
                    cate_Tarea = 'Hogar'
                elif cate_Tarea == 6:
                    cate_Tarea = 'Finanzas'
                elif cate_Tarea is None:
                    pass
                else:
                    print(f"El numero {prio_Tarea} no es una opción, por favor Selecciona una opción (1-6): ")
                
                '''Todas las tarea agregada deben tener el estado Pendiente | En el campo Update van los demás 
                campo y una condición que cuando se cumpla la fecha de vencimiento cambie de esta y se termine
                est_Tarea = [
                    "Estado de las Tareas: ",
                    '1. Pendiente', # La tarea aún no ha comenzado.
                    '2. En Progreso', # La tarea está en proceso de realización.
                    '3. En Espera',#La tarea está en pausa o esperando información adicional.
                    '4. Completada',#La tarea ha sido finalizada y está completa.
                    '5. Cancelada' # La tarea ha sido cancelada y no se completará.
                ]
                print('\n'.join(est_Tarea))# formateamos la salida de la lista
                est_Tarea = solicitar_input("Selecciona una opción (1-5): ",int) # Menu de Estado
                if est_Tarea == 1:
                    est_Tarea = 'Pendiente'
                elif est_Tarea == 2:
                    est_Tarea = 'En Progreso'
                elif est_Tarea == 3:
                    est_Tarea = 'En Espera'
                elif est_Tarea == 4:
                    est_Tarea = 'Completada'
                elif est_Tarea == 5:
                    est_Tarea = 'Cancelada' '''
                
                tareAg = {
                    '_id' : genera_id(),
                    'Título': nom_Tarea,
                    'Descripción': desc_Tarea,
                    'Fecha de Vencimiento': fech_Vence.strftime('%Y-%m-%d %H:%M:%S'),
                    'Prioridad': prio_Tarea, 
                    'Categoría': cate_Tarea, 
                    'Estado': 'Pendiente', 
                    'Fecha de Creación': fech_Creada.strftime('%Y-%m-%d %H:%M:%S')
                } 
                
                try: # investigar try 
                    dbTabla.insert_one(tareAg)
                    print(f'Documento insertado con ID específico: {tareAg["_id"]}')
                except Exception as e:
                    print(f'Error al insertar documento: {e}')
            break # Salir del bucle una vez que se hayan agregado las tareas
        elif numTarea is None : # todas la funcion devuelven un valor y no quiero que NOne salga en ninguno de los print
            pass
        else:
            print("Por favor, Ingresar un Valor Mayor que 0.")

#agregarTarea()

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