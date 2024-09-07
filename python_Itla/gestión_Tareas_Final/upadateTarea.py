from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017') # Conectar al servidor de MongoDB
db = client['Gestión_de_Tareas'] # Seleccionar la base de datos
dbTabla = db['TablaGESTION'] # Seleccionar la colección(Tabla)


'''def mostrar_primeros_10_registros():
    registros = dbTabla.find().limit(10)
    for registro in registros:
        print(registro)'''

def mostrar_primeros_10_registros():
    registros = dbTabla.find().limit(10)
    for i, registro in enumerate(registros, start=1):
        id_ = registro.get('_id', 'N/A')
        nombre = registro.get('Título', 'N/A')
        descripción = registro.get('Descripción', 'N/A')
        fechaFin = registro.get('Fecha de Vencimiento', 'N/A')
        # Agrega aquí los campos que deseas mostrar
        print(f'Registro {i}:')
        print(f'  ID: {id_}')
        print(f'  Título: {nombre}')
        print(f'  Descripción: {descripción}')
        print(f'  Fecha de Vencimiento: {fechaFin}')
        # Imprime otros campos aquí si es necesario
        print('-' * 20)

# Ejemplo de uso
mostrar_primeros_10_registros()

def actualizarTarea():
    # Realizar una búsqueda
    titulo = input("\n Ingrese el Título(Nombre) de la búsqueda: ").lower()
    busca = {'Título': titulo}
    resultado = dbTabla.find(busca)
    
    for documento in resultado:
        formato = [f"{clave}: {valor}" for clave, valor in documento.items()]
        formato = '\n'.join(formato)
        print('\n', formato, '\n')
actualizarTarea()