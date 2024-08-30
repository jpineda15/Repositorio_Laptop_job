# Importamos las Funciones que imprimen los Registro de los Estudiantes. 
from funciones import imprimir_información_estudiante, procesar_estudiantes

# Creamos la Lista estudiante con los diccionarios que contienen la información de los Estudiantes. 
estudiantes = [
    {'Nombre' : "John Manuel", 'Edad' : 17, 'Curso' : "2-A", 'Pro_Calificación' : 8.3},
    {'Nombre' : "Adriel Francisco", 'Edad' : 15, 'Curso' : "1-B", 'Pro_Calificación' : 9.5},
    {'Nombre' : "Natalicia", 'Edad' : 14, 'Curso' : "2-c", 'Pro_Calificación' : 8.0},
    {'Nombre' : "Zabdiel De Jesus", 'Edad' : 19, 'Curso' : "4-A", 'Pro_Calificación' : 8.6},
    {'Nombre' : "Pedro Santos", 'Edad' : 13, 'Curso' : "1-c", 'Pro_Calificación' : 7.8},
    {'Nombre' : "Marta Cordero", 'Edad' : 17, 'Curso' : "3-A", 'Pro_Calificación' : 8.3},
]


# Creamos un Bucle for para iterar la Lista con los diccionarios
for lista in estudiantes:
    # formateamos el contenido del diccionario(lista) que contiene la información de los estudiantes a
    # la Variable Lista con el contenido formateado
    lista =  ', '.join([f'{clave}: {valor}' for clave, valor in lista.items()])
    # llamamos esta función para que procese la información que obtiene la variable lista
    imprimir_información_estudiante(lista)

print("##########################################################################")

# llamamos esta función y pasamos la lista estudiantes
procesar_estudiantes(estudiantes)


"""
Tarea Mod-7
    Registro de Estudiantes - Modularizado

    Crea una lista que contenga diccionarios representando estudiantes. Cada diccionario debe contener información como:
    nombre, edad, curso y promedio de calificaciones. Luego, utiliza un bucle para recorrer la lista e imprimir la información de cada estudiante.

Ojo a los detalles:
    -Debes estar Modularizado por los archivos(funciones.py y main.py)
    -En funciones.py debes crear dos funciones (imprimir_información_estudiante y
    procesar_estudiantes).
    -La función imprimir_información_estudiante debe recibir un parámetro (estudiante)
    e imprimir cada registro o diccionario.
    -La función procesar_estudiantes debe recibir un parámetro(estudiante)
    y recorrer la lista completa llamando a la imprimir_información_estudiante
    para mostrarlo
    -En main.py debe importar solo la función a utilizar, no el módulo completo
    -Pasar por lo menos 5 diccionarios


Registro de Estudiantes (Algoritmo Informal):

    Archivo main.py

        1.	Importar las Funciones a utilizar:
                A.	imprimir_información_estudiante
                B.	procesar_estudiantes
        2.	Se creo una lista:
                A.	estudiantes: esta almacena Varios diccionarios.
                    a.	Nombre, Edad, Curso, Promedio de Calificaciones.
        3.	Se creo un bucle for para iterar la lista:
                A.	Formateamos la información que nos facilita el bucle en cada vuelta.
                B.	Asignamos esa información a una variable.
                C.	Llamamos la función: 
                    a.	imprimir_información_estudiante(): pasar parámetro(variable con información formateada)
        4.	Llamamos la función: procesar_estudiantes(estudiantes) y pasar parámetro(lista con diccionario).

    Archivo funciones.py

        1.	Se creo una función:
                A.	imprimir_información_estudiante(estudiante): esta función recibe un parámetro.
                    a.	Imprimir el argumento que recibe.	
        2.	Se creo una función:
                A.	procesar_estudiantes(estudiantes): esta función recibe un parámetro.
                    a.	 Creamos un bucle for para iterar los argumento recibido.
                        1.	Llamamos la función imprimir_información_estudiante(estudiante)

"""