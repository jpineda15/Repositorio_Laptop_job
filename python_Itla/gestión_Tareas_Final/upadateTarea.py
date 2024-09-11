from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor
from datetime import datetime
from opciones import prioridadF, categoríaF # type: ignore

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017') # Conectar al servidor de MongoDB
db = client['Gestión_de_Tareas'] # Seleccionar la base de datos
dbTabla = db['TablaGESTION'] # Seleccionar la colección(Tabla)



def actualizarTarea():
    # Realizar una búsqueda
    id_registro = input("\n Ingrese el número de ID GT-: ")
    #id_registro = f"GT-{numero_adicional}" 
    
    busca = {'_id': id_registro}
    resultado = dbTabla.find(busca)
    
    for documento in resultado:
        formato = [f"{clave}: {valor}" for clave, valor in documento.items()]
        formato = '\n'.join(formato)
        print('\n', formato, '\n')
    
    print("\n Que campo desea actualizar.")
    myOption = [
        '1. Título',
        '2. Descripción',
        '3. Fecha de Vencimiento',
        '4. Categoría',
        '5. Prioridad',
        '6. Estado'
    ]
    print('\n','\n'.join(myOption))
    
    while True:
        try:
            updateOpt = int(input("\nSelecciona una opción (1-6). Para Salir Ingrese 0: "))
        except ValueError:
            print("\nPor favor ingresa un número válido.")
            continue
        
        if updateOpt == 1:
            campo = 'Título'
            newVolor = input(f"Ingrese el nuevo valor para {campo}: ")
            actuli = {'$set': {campo: newVolor}}
            resultado = dbTabla.update_one(busca, actuli)
            
        elif updateOpt == 2:
            campo = 'Descripción'
            newVolor = input(f"Ingrese el nuevo valor para {campo}: ")
            actuli = {'$set': {campo: newVolor}}
            resultado = dbTabla.update_one(busca, actuli)
            
        elif updateOpt == 3:
            campo = 'Fecha de Vencimiento'
            newValor = input(f"Ingrese la nueva fecha y hora para '{campo}' en formato YYYY-MM-DD HH:MM:SS: ")
            try:
                newH = datetime.strptime(newValor, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print("Formato de fecha y hora inválido. Por favor use YYYY-MM-DD HH:MM:SS.")
                return
            actuli = {'$set': {campo: newH}}
            
        elif updateOpt == 4:
            valor = categoríaF() # Llamos la fucion de las Característica
            campo = 'Categoría'
            
            actuli = {'$set': {campo: valor}} # Crea el diccionario de actualización
            resultado = dbTabla.update_one(busca, actuli)
            
        resultado = dbTabla.find(busca)
        for documento in resultado:
            formato = [f"{clave}: {valor}" for clave, valor in documento.items()]
            formato = '\n'.join(formato)
            print('\n Vista actualizada: \n', formato, '\n')
        break
#actualizarTarea()
