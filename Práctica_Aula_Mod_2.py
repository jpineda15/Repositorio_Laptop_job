#Práctica en el aula Mod-2

# Calcula el año en el que la persona cumplirá 100 años.

def cien_year(): # Creamos la Funcion cien_year
    año = int(input("Ingrese el año de Nacimiento: ")) # Solicitamos al Usuario que ingrese el Año de Nacimiento
    cien_años = año + 100 # Calculamos el año en que el Usuario cumplirá 100 año
    print("Usted Cumplirá 100 años en el año", cien_años) # Imprimimos el resultado
cien_year() # Llamamos la funcion que contiene el bloque de codigo