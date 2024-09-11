import sqlite3

ruta_db = "gestorTarea.db"
try:
    my_conexion = sqlite3.connect(ruta_db)
    
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
except Exception as ex:
    print(ex)