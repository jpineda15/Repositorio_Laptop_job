'''
Venta de Alcohol:
    Pregunta al usuario su edad.
    Utiliza un operador lógico para determinar si el usuario tiene la edad suficiente para comprar.
    alcohol en función de la legislación local (por Ejemplo, 18 años). 
    Muestra un mensaje indicando si el salario puede comprar alcohol o no.
'''

''' 
    Algoritmo Informal pra Verificar la edad y permitir la compra de Alcohol
            1.  Imprimir "No vendemos Alcohol a Menores".
            2.  Dejar una linea en blanco: para mejor visualización.
            3.  Pedir al usuario que ingrese su edad y Convertir la edad a número entero.
            4.  Si la edad es 18 o más, Imprimir "Eres mayor de edad. Puedes comprar bebidas alcohólicas."
            5.  Si la edad es menor de 18, Imprimir "No tienes la edad suficiente para comprar bebidas alcohólicas."
            6.  Imprimir "Gracias por preferirnos".
            7.  Ejecutar la función comp_alco() para iniciar el proceso.
'''

# Proceso 
def comp_alco():
    print("No vendemos Alcohol a Menores")
    print() #quiero un espació en blanco
    edad = int(input("Por favor, ingrese su edad: "))
    if edad >= 18:
        print("Eres mayor de edad. Puedes comprar bebidas alcohólicas.")
    else:
        print("No tienes la edad suficiente para comprar bebidas alcohólicas.")
    print("Gracias por preferirnos")
comp_alco() # llamamos la función 




print("Práctica en el aula Mod-3(ext-2) --> Aprobación de Crédito")

'''
Aprobación de Crédito:
    pregunta al usuario si tiene un trabajo estable (si/no). --> "Sin diferencia entre minúsculas y mayúsculas ("sI/No")"
    pregunta al usuario si tiene un buen historial crediticio (si/no).
    utiliza un operador lógico  para determinar si el usuario es elegible para obtener un Crédito
    Muestra un mensaje indicando si el usuario es elegible o no. 
'''

'''
    Algoritmo Informal para Aprobación de Crédito:
        1.  Creamos una Función que contenga todo el código.
        2.  Pedimos al usuario que ingrese si tiene un trabajo estable (si/no). 
        3.  Pedimos al usuario que ingrese si tiene un buen historial crediticio (si/no).
        4.  Convertimos a minúscula el valor de las variables job y credit (si/no) 
        5.  Si el usuario tiene un trabajo estable y un buen historial crediticio, Imprimir "Usted es elegible para obtener un Crédito"
        6.  Si no se cumple con cualquiera de esta dos condiciones, Imprimir "Usted no es elegible para obtener un Crédito"
        7.  Ejecutar la función apro_cred() para iniciar el proceso.
'''

# Proceso
def apro_cred():
    job = input("¿Tiene un trabajo estable? (Si/No): ")
    credit = input("¿Tiene un buen historial crediticio? (Si/No): ")
    joB = job.lower() # convertir el valor de job a minúsculas 
    crediT = credit.lower() # convertir el valor de credit a minúsculas 
    if joB == True and crediT == True: # Validar si ambas variables son verdaderas 
        print("Usted es elegible para obtener un Crédito")
    else:
        print("Usted no es elegible para obtener un Crédito")
apro_cred()
