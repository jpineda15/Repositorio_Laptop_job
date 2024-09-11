from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor
from opciones import prioridadF, categoríaF # type: ignore


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
    
    while True:
        filtro_Tarea = prioridadF() # Llamos la funcion de las Prioridades
        
        registros = list(dbTabla.find({'Prioridad': filtro_Tarea}).limit(5)) # Consultamso la Prioridad selecionada 
        
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
            break # Salir del bucle si hay registro
        else:
            print(f"\n No hay tareas con prioridad asignada como: '{filtro_Tarea}'.")

