'''def hola(mensaje, tipo_dato=int):
    contador = 0
    intentos=3
    while contador < intentos:
        try:
            valor = tipo_dato(input(mensaje))
            return valor
        except ValueError:
            contador += 1
            print(f"El valor ingresado no es válido. Te quedan {intentos - contador} intento(s). Por favor, ingresa un valor correcto.")
    
    print("Has alcanzado el número máximo de intentos. El sistema se cerrará...")
    
    return None  # Retorna None si no se obtiene un valor válido'''


def solicitar_input(mensaje, tipo_dato ):
    contador =0
    intentos = 3
    
    while contador < intentos:
        try:
            valor = tipo_dato(input(mensaje))
            return valor
        except ValueError:
            contador += 1
            print(f"El valor ingresado no es válido. Te quedan {intentos - contador} intento(s). Por favor, ingresa un valor correcto.")
    print("Has alcanzado el número máximo de intentos (3). El sistema se cerrará...")

# Ejemplo de uso
num_tarea = solicitar_input("Indique la cantidad de tareas que desea agregar: ", int)
#otra_tarea = solicitar_input("Indique la cantidad de tareas que desea agregar: ", int)
