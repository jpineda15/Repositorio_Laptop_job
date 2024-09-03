from pymongo import MongoClient 

# Conectar al servidor de MongoDB
client = MongoClient('mongodb://localhost:27017')

# Seleccionar la base de datos
db = client['Gestión_de_Tareas']

# Seleccionar la colección
dbTabla = db['Tareas']

# Diccionario a insertar
gestorD = {
    'Título': 'Mango',
    'Descripción': 'Mango maduro',
    'Prioridad': 'Alta',
    'Categoría': 'Personal',
    'Estado': 'En Proceso'
}

# Insertar el diccionario en la colección
resultado = dbTabla.insert_one(gestorD)

# Imprimir el ID del documento insertado
print(f'Diccionario insertado con ID: {resultado.inserted_id}')
