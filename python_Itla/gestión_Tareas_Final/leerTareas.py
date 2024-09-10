from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor
from funcionAgre import solicitar_input


# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017') # Conectar al servidor de MongoDB
db = client['Gestión_de_Tareas'] # Seleccionar la base de datos
dbTabla = db['TablaGESTION'] # Seleccionar la colección(Tabla)

def vistaGeneral():
    # Limita los resultados a 5 registros desde la base de datos
    vista = dbTabla.find().limit(5)
    for a, ver in enumerate(vista, start=1):
        # Obtiene los valores de cada registro, con "N/A" como valor predeterminado si la clave no existe
        _id = ver.get('_id', 'N/A')
        nombre = ver.get('Título', 'N/A')
        descripcion = ver.get('Descripción', 'N/A')
        fechaFin = ver.get('Fecha de Vencimiento', 'N/A')
        prioridad = ver.get('Prioridad', 'N/A')
        categoría = ver.get('Categoría', 'N/A')
        estado = ver.get('Estado', 'N/A')
        fechCrea = ver.get('Fecha de Creación', 'N/A')

        # Imprime la información formateada
        print(f'\nRegistro {a}:')
        print(f'  ID: {_id}')
        print(f'  Título: {nombre}')
        print(f'  Descripción: {descripcion}')
        print(f'  Fecha de Vencimiento: {fechaFin}')
        print(f'  Prioridad: {prioridad}')
        print(f'  Prioridad: {categoría}')
        print(f'  Prioridad: {estado}')
        print(f'  Prioridad: {fechCrea}')
        print('-' * 20)
    print("\n Vista de los 05 Primeros Registros. ")



# Imprimir registro almacenado
def mostrar_registros():
    vistaGeneral()
    filtro_Tarea = [
                'Filtrar por Prioridad: ',
                '1. Alta', #Tareas críticas que deben ser atendidas inmediatamente.
                '2. Media', #Tareas importantes, pero que no requieren atención inmediata.
                '3. Baja', #Tareas que pueden esperar o que no tienen una urgencia particular.
                '4. Crítica' #Tareas que son absolutamente esenciales y que, si no se completan, pueden tener un impacto significativo en el proyecto o negocio.
                ]
    
    print('\n','\n'.join(filtro_Tarea)) # formateamos la salida de la lista 
    filtro_Tarea = solicitar_input("\nSeleccione una opción (1-4) para ordenar. Para volver al inicio, ingrese 0: ",int) # Menu de Prioridad
    
    if filtro_Tarea == 1:
        filtro_Tarea = "Alta"
    elif filtro_Tarea == 2:
        filtro_Tarea = "Media"
    elif filtro_Tarea == 3:
        filtro_Tarea = 'Baja'
    elif filtro_Tarea == 4:
        filtro_Tarea = 'Crítica'
    elif filtro_Tarea is None:
        pass
    elif filtro_Tarea == 0: # Volver al menu Inicio
        from menu import menuInicio
        menuInicio()
        return
    else:
        print(f"\n El numero {filtro_Tarea} no es una opción, por favor Selecciona una opción (1-4): ")
    
    
    #registros = dbTabla.find({'Prioridad': filtro_Tarea}).limit(5) # Ralizamos una busqueda en la DB y limitamos a 5 registro
    registros = list(dbTabla.find({'Prioridad': filtro_Tarea}).limit(5))
    
    
    
    if len(registros) > 0: # Verificamos si hay registros
        for i, registro in enumerate(registros, start=1): # iteramos sobre los registro y los enumeramos (enumerate) iniciando en 1
            
            # Realizamos la busqueda de los registro deseado (get) y si no se encuentra lo sustituye con (N/A)
            id_ = registro.get('_id', 'N/A')
            nombre = registro.get('Título', 'N/A')
            descripción = registro.get('Descripción', 'N/A')
            fechaFin = registro.get('Fecha de Vencimiento', 'N/A')
            prioridad = registro.get('Prioridad', 'N/A')
            
            # Agrega aquí los campos que deseas mostrar
            print(f'\n Registro {i}:')
            print(f'  ID: {id_}')
            print(f'  Título: {nombre}')
            print(f'  Descripción: {descripción}')
            print(f'  Fecha de Vencimiento: {fechaFin}')
            print(f'  Prioridad: {prioridad}')
            # Imprime otros campos aquí si es necesario
            print('-' * 20) # limite de separacion entre cad registro
            
    else:
        print(f"\n No hay tareas con prioridad asignada como: '{filtro_Tarea}'.")
        
        mostrar_registros() # Leer y filtrar tarea almacenada 



# Ejemplo de uso
#mostrar_registros()