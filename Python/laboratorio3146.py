"""
3.1.4.6 LAB: Conceptos básicos de listas
"""
def listas():
    hatList = [1, 2, 3, 4, 5]
    print(f"Lista Inicial: {' '.join(map(str, hatList))}")
    hatList[2] = int(input("Ingrese un Numero Entero: "))
    del hatList[-1]
    print(f"Lista Final: {' '.join(map(str, hatList))}")
    print(f"Total de Elementos en la Lista: {len(hatList)}")
listas()