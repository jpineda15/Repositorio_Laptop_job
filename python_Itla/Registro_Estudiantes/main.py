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