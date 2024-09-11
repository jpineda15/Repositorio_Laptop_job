import sqlite3
import os

db_path = "PythonGit\python_Itla\gestión_Tareas_Final\database\gestorTarea.db"

try:
    if not os.path.exists(db_path):
        my_conexion = sqlite3.connect(db_path)
        cursor = my_conexion.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS gestion (
                    _id TEXT PRIMARY KEY,
                    Título TEXT,
                    Descripcion TEXT,
                    Fecha_Vencimiento DATE,
                    Prioridad TEXT,
                    Categoría TEXT,
                    Estado TEXT,
                    Fecha_Creación DATE
                )
            ''')
        my_conexion.commit()
        print("Tabla creada exitosamente.")
    else:
        print(f"El archivo de la base de datos '{db_path}' ya existe.")
except Exception as ex:
    print(f"Ocurrió un error: {ex}")
