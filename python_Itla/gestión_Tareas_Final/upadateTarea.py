from pymongo import MongoClient  # Importar el cliente de MongoDB para conectarse al servidor
from funcionAgre import solicitar_input
from datetime import datetime
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
        '4. Prioridad',
        '5. Categoría',
        '6. Estado'
    ]
    print('\n','\n'.join(myOption))
    updateOpt = solicitar_input("\nSelecciona una opción (1-6): ",int)
    
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
        newVolor = input(f"Ingrese la nueva fecha y hora para '{campo}' en formato YYYY-MM-DD HH:MM:SS: ")
        try:
            newH = datetime.strptime.(newValor, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print("Formato de fecha y hora inválido. Por favor use YYYY-MM-DD HH:MM:SS.")
            return
        nuevoh = newH
        actuli = {'$set': {campo: nuevoh}}
    elif updateOpt == 4:
        campo = 'Prioridad'
        cate_Tarea = [
            "Característica de las Tareas: ",
            '1. Trabajo',
            '2. Personal',
            '3. Urgente',
            '4. Estudios',
            '5. Hogar',
            '6. Finanzas'
            ]
        print('\n'.join(cate_Tarea)) 
        categoria_seleccionada = solicitar_input("Selecciona una opción (1-6): ", int)
        categorias = {
            1: "Trabajo",
            2: "Personal",
            3: "Urgente",
            4: "Estudios",
            5: "Hogar",
            6: "Finanzas"
        }
        cate_Tarea = categorias.get(categoria_seleccionada, "Opción inválida")
        actuli = {'$set': {campo: cate_Tarea}}
        resultado = dbTabla.update_one(busca, actuli)
#actualizarTarea()
