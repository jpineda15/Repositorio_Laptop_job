''' 
    3.1.2.9 LAB: La declaración de ruptura - Atascado en bucle
'''
def infinito():
    while True:
        word = input("Ingresa la Palabra Secreta para salir del Loop: ")
        if word == "chupacabra":
            break
    print("Felicidades! Has salido del Loop.")
infinito()