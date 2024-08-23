'''
3.1.2.3 LAB: Conceptos básicos del bucle while - Adivina el numero secreto
'''

def numSecreto():
    print(
        '''
        Bienvenido al juego de adivina el número secreto.
        ''')
    secret_number = 777
    user_number = int(input("Ingrese un Numero: "))
    while user_number != secret_number:
        print("Ha ha! You`re stuck in my loop!")
        user_number = int(input("Ingrese un Numero: "))
    print(secret_number, "Well done muggle! You are free now.")
numSecreto()  # Llamada a la función para ejecutar el programa.