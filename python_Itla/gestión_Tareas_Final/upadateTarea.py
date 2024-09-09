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