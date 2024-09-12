import sqlite3

# Ruta de la base de datos
ruta_db = "PythonGit/python_Itla/gestión_Tareas_Final/database/gestorTarea.db"

def eliminar_registro():
    try:
        # Conexión a la base de datos
        my_conexión = sqlite3.connect(ruta_db)
        cursor = my_conexión.cursor()
        
        id_registro = input("\nIngrese el número de ID GT-: ")
        # Validación del input para asegurarse de que es un número
        
        # Consulta SQL para eliminar un registro
        consulta = "DELETE FROM GESTION WHERE _id = ?"
        cursor.execute(consulta, (id_registro,))
        
        # Verificación si se eliminó algún registro
        if cursor.rowcount == 0:
            print(f"No se encontró ningún registro con ID {id_registro}.")
        else:
            print(f"Registro con ID {id_registro} eliminado exitosamente.")
        
        # Guardar los cambios
        my_conexión.commit()
            
    except sqlite3.Error as error:
        print("Error al eliminar el registro:", error)
    
    finally:
        # Asegurarse de cerrar la conexión
        if my_conexión:
            my_conexión.close()


