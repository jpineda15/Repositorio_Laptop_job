from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017') # Conectar al servidor de MongoDB
db = client['Gestión_de_Tareas'] # Seleccionar la base de datos
dbTabla = db['TablaGESTION'] # Seleccionar la colección(Tabla)


def actualizarTarea():
    # Realizar una búsqueda
    numero_adicional = input("\n Ingrese el número de ID GT-: ")
    id_registro = f"GT-{numero_adicional}" 
    
    busca = {'_id': id_registro}
    resultado = dbTabla.find(busca)
    
    for documento in resultado:
        formato = [f"{clave}: {valor}" for clave, valor in documento.items()]
        formato = '\n'.join(formato)
        print('\n', formato, '\n')
#actualizarTarea()



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