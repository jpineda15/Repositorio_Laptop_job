from datetime import datetime, timedelta # Importamos la clase datetime & timedelta
import 
"""
    datetime -->Esta clase se utiliza para manejar fechas y horas. Proporciona métodos para obtener la fecha y hora actual.
    timedelta -->Esta clase representa una duración o diferencia entre dos fechas o tiempos. Se utiliza para realizar operaciones aritméticas con fechas y horas, como sumar o restar días, horas, minutos, segundos, etc., a un objeto datetime.

"""
id_Tareas = 1 # Declaramos una variable global. 
"""
Agrega una variable global para el contador de IDs: 
Puedes definir una variable fuera de la función agregarTarea() para mantener el estado del contador.
"""

# Función para control de error al ingresar de valores por teclado

def solicitar_input(mensaje, tipo_dato): # mensaje --> Muestra el mensaje del input | tipo_dato --> recibe el valor ingresado
    contador =0
    intentos = 3
    
    while contador < intentos:
        try:
            valor = tipo_dato(input(mensaje))
            return valor
        except ValueError:
            contador += 1
            print(f"El valor ingresado no es válido. Te quedan {intentos - contador} intento(s). Por favor, ingresa un valor correcto.")
    print("Has alcanzado el número máximo de intentos. El sistema se cerrará...")


# Agregar Tareas
def agregarTarea():
    
    global id_Tareas  # Usar el contador global
    
    tareAg = {}
    
    fech_Creada = datetime.now() # Obtenemos la Fecha de Creación de la tarea
    fech_Vence = fech_Creada + timedelta(days=30) # Obtenemos la Fecha en la que se vence la tarea (OJO realizar condición que cambie a estado terminado si se cumple esta fecha)
    
    while True:
        # llamamos la función solicitar_input y solicitar el ingreso de la cantidad de tarea a crear.
        numTarea = solicitar_input("Indique la Cantidad de Tarea desea Agregar: ", int) 
        
        # Agregar todos que se se ingresa por teclado al diccionario tareAg (OJO)
        """
        
        """
        if numTarea is not None and numTarea > 0: # No comparar TypeError(None) y Mayor que 0
            
            print("---Agregando Nueva Tareas---")
            
            for c in range(0, numTarea): # tengo duda validar
                
                nom_Tarea = input("Título de la Tarea: ") # Ingresar titulo de la tarea
                
                if nom_Tarea in tareAg: # si se cumple obviara todo lo siguiente y iniciara nuevamente el bucle for
                    print(f"La tarea '{nom_Tarea}' ya existe")
                    continue 
                
                desc_Tarea = input("Ingrese una Breve descripción de la Tarea: ") # Ingresar una descripción de la tarea
                
                prio_Tarea = [
                    'Prioridades de las Tareas: ',
                    '1. Alta',
                    '2. Media',
                    '3. Baja'
                ]
                print('\n'.join(prio_Tarea)) # formateamos la salida de la lista 
                prio_Tarea = solicitar_input("Selecciona una opción (1-3): ",int) # Menu de Prioridad
                
                cate_Tarea =[
                    "Característica de las Tareas: ",
                    '1. Trabajo', #Tareas relacionadas con el empleo, proyectos laborales, reuniones, etc.
                    '2. Personal', #Actividades personales como citas médicas, eventos familiares, o autocuidado. 
                    '3. Urgente ', #Tareas que requieren atención inmediata o de alta prioridad.
                    '4. Estudios ', #Tareas relacionadas con la educación, como exámenes, deberes o proyectos académicos.
                    '5. Hogar', #Actividades relacionadas con el mantenimiento del hogar, como limpieza, reparaciones o compras domésticas.
                    '6. Finanzas' #Tareas relacionadas con la gestión de dinero, pagos, presupuestos, etc.
                ]
                print('\n'.join(cate_Tarea))# formateamos la salida de la lista
                cate_Tarea = solicitar_input("Selecciona una opción (1-6): ",int) # Menu de Categoría
                
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
                
                
                tareAg[id_Tareas] = {
                    'Título': nom_Tarea,
                    'Descripción': desc_Tarea,
                    'Fecha de Vencimiento': fech_Vence.strftime('%Y-%m-%d %H:%M:%S'),
                    'Prioridad': prio_Tarea, #[prio_Tarea - 1].split('. ')[1] if 1 <= prio_Tarea <= 3 else 'Desconocida',
                    'Categoría': cate_Tarea, #[cate_Tarea - 1].split('. ')[1] if 1 <= cate_Tarea <= 6 else 'Desconocida',
                    'Estado': est_Tarea, #[est_Tarea - 1].split('. ')[1] if 1 <= est_Tarea <= 5 else 'Desconocido',
                    'Fecha de Creación': fech_Creada.strftime('%Y-%m-%d %H:%M:%S'),
                }
                
                id_Tareas += 1 # Incrementar el contador. 
                #print(f"Tarea '{nom_Tarea}' con '{id_Tareas}' fue añadida correctamente.")
                print(tareAg)
            break # Salir del bucle una vez que se hayan agregado las tareas
        else:
            print("Por favor, Ingresar un Valor Mayor que 0.")
'''    
    tareAg = { # OJO el ID o contador_ID debe corregirlo 
        'Titulo' : nom_Tarea,
        'Descripción' : desc_Tarea,
        'Fecha de Vencimiento' : fech_Vence.strftime('%Y-%m-%d %H:%M:%S'), #La fecha límite para completar la tarea
        'Prioridad' : prio_Tarea, #Nivel de urgencia de la tarea (por ejemplo, baja, media, alta)
        'Categoría' :cate_Tarea, # Opciones para clasificar la tarea dentro de una o más categorías (por ejemplo, "Trabajo", "Personal", "Urgente"). Esto facilita el filtrado y la organización de las tareas.
        'Estado' : opción03, # Estado actual de la tarea (por ejemplo, pendiente, en progreso, completada, Terminada).
        'Fecha de Creación' : fech_Creada.strftime('%Y-%m-%d %H:%M:%S'), # Fecha de creación 
        }
'''

agregarTarea()

"""
1- id_contador: Variable global que se usa para asignar un ID único a cada tarea.
2- global id_contador: Se declara dentro de la función para modificar la variable global.
3- tareAg[id_contador]: Utiliza id_contador como clave en el diccionario para asegurar que cada tarea tenga un ID único.
4- id_contador += 1: Incrementa el contador después de agregar una tarea.
"""