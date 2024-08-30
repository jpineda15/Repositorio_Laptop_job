
# Creamos una función que reciba un parámetro e imprimir. 
def imprimir_información_estudiante(estudiante):
    print(f"Estudiante: {estudiante}.")
    #return estudiante

# Creamos una función que reciba un parámetro.
def procesar_estudiantes(estudiantes):
    # crear bucle para iterar la información recibida
    for estudiante in estudiantes:
        # Llamamos esta función y pasamos la información deseada
        imprimir_información_estudiante(estudiante)

