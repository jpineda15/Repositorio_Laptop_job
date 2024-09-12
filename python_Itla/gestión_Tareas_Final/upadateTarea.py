from opciones import prioridadF, categoríaF, estadoF # Del módulo opciones.py importamos las Funciones prioridadF, categoríaF & estadoF
import sqlite3 # Importa el módulo sqlite3 para trabajar con bases de datos SQLite

# Ruta de la base de datos
ruta_db = "PythonGit/python_Itla/gestión_Tareas_Final/database/gestorTarea.db"

# Inicialización de las variables para la conexión y el cursor
my_conexión = None
cursor = None


# Solicitar la inserción de un valor entero por teclado 
def controlError(mensaje):
    while True:
        # Este control de excepciones verifica que la entrada sea un número, de lo contrario muestra un error y solicita nuevamente si no lo es.
        try:
            valor = int(input(f"\n{mensaje}"))
            return valor
        except ValueError:
            print("Por favor ingresa un número válido.")


def actualizarTarea():
    try:
        # Conectar a la base de datos con un timeout de 10 segundos
        my_conexión = sqlite3.connect(ruta_db, timeout=10)
        my_conexión.row_factory = sqlite3.Row
        cursor = my_conexión.cursor()
        
        id_registro = input("\nIngrese el número de ID GT-: ")
        
        # Consulta para obtener los registros
        consulta = "SELECT * FROM GESTION WHERE _id = ?"
        cursor.execute(consulta, (id_registro,))
        resultado = cursor.fetchall()
        
        
        # Formatear y mostrar los resultados como diccionarios
        for documento in resultado:
            formato = [f"{clave}: {valor}" for clave, valor in dict(documento).items()]
            print('\n', '\n'.join(formato), '\n')
        
        print("\nQué campo desea actualizar.")
        miOption = [
            '1. Título',
            '2. Descripción',
            '3. Fecha_Vencimiento',
            '4. Categoría',
            '5. Prioridad',
            '6. Estado'
        ]
        print('\n', '\n'.join(miOption))
        
        while True:
            updateOpt = controlError("Selecciona una opción (1-6). Para Salir Ingrese 0: ")
            
            if updateOpt == 0:
                print("Saliendo...")
                break
            
            if updateOpt < 1 or updateOpt > 6:
                print("\nPor favor ingresa una opción válida entre 1 y 6.")
                continue
            
            # creamos un diccionario con los campo de la DB que vamos a modificar
            campos = {
                1: 'Título',
                2: 'Descripción',
                3: 'Fecha_Vencimiento',
                4: 'Categoría',
                5: 'Prioridad',
                6: 'Estado'
            }
            
            campo = campos[updateOpt]
            
            # Solicitar nuevo valor según el campo seleccionado
            if updateOpt == 1:
                new_valor = input(f"Ingrese el nuevo valor para {campo}: ")
            elif updateOpt == 2:
                new_valor = input(f"Ingrese el nuevo valor para {campo}: ")
            elif updateOpt == 3:
                new_valor = input(f"Ingrese el nuevo valor para {campo} (YYYY-MM-DD HH:MM:SS): ")
            elif updateOpt == 4:
                new_valor = categoríaF()
            elif updateOpt == 5:
                new_valor = prioridadF()
            elif updateOpt == 6:
                new_valor = estadoF()
            
            # Actualizar el registro en la base de datos
            sql_update = f"UPDATE GESTION SET {campo} = ? WHERE _id = ?"
            cursor.execute(sql_update, (new_valor, id_registro))
            my_conexión.commit()
            
            # Consultar y mostrar el registro actualizado
            cursor.execute(consulta, (id_registro,))
            registro_actualizado = cursor.fetchone()
            
            if registro_actualizado:
                formato = [f"{clave}: {valor}" for clave, valor in dict(registro_actualizado).items()]
                print('\nRegistro Actualizado:\n', '\n'.join(formato), '\n')
            break
    
    except Exception as ex:
        print("Error:", ex)
    finally:
    # Cerrar el cursor y la conexión a la base de datos si están abiertos
        if cursor:
            cursor.close()
        if my_conexión:
            my_conexión.close()

#GT-240911152230
