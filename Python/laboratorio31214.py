"""
3.1.2.14 LAB: Conceptos básicos del bucle while
"""

def alturas():
    blocks = int(input("Ingrese el Numero de blocks: "))
    altura = 0
    capas = 1
    while capas <= blocks:
        altura += 1
        blocks -= capas
        capas += 1
    print("La Altura de la pirámide", altura)
alturas()
