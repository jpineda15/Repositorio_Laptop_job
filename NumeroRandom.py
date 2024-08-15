"""
Imprimir números Aleatorios. 

Kino TV --> prueba
"""

"""import random

get_Num = []

for i in range(1, 21):
    n = random.randint(1, 80)
    get_Num.append(n)
lista2 = []

for p in get_Num:
    lista2.append(p)
lista2.sort()
print(lista2)"""

"""import random

# Generar una lista de 20 números aleatorios entre 1 y 80
get_Num = [random.randint(1, 80) for _ in range(20)]

# Ordenar la lista
lista2 = sorted(get_Num)

# Convertir la lista en cadenas y unir los elementos
cadena1 = " ".join(map(str, get_Num))
cadena2 = " ".join(map(str, lista2))

# Imprimir las dos cadenas
print("Cadena original:", cadena1)
print("Cadena ordenada:", cadena2)"""


'''''import random

# Generar la primera combinación de 10 números aleatorios entre 1 y 80
combinación1 = set(random.randint(1, 80) for _ in range(10))

# Generar una segunda combinación distinta de 20 números aleatorios entre 1 y 80
combinación2 = set(random.randint(1, 80) for _ in range(10))

# Generar una tercera combinación distinta de 20 números aleatorios entre 1 y 80
combinación3 = set(random.randint(1, 80) for _ in range(10))

# Convertir las listas en cadenas y unir los elementos
cadena1 = " ".join(map(str, combinación1))
cadena2 = " ".join(map(str, combinación2))
cadena3 = " ".join(map(str, combinación3))

# Imprimir las dos combinaciones
print("Primera combinación:", cadena1)
print("Segunda combinación:", cadena2)
print("Segunda combinación:", cadena3)'''''



"""import random

def generar_combinación(excluidos):
    combinación = set()
    while len(combinación) < 10:
        num = random.randint(1, 80)
        if num not in excluidos:
            combinación.add(num)
    return combinación

# Generar la primera combinación de 10 números aleatorios entre 1 y 80
combinación1 = generar_combinación(set())

# Generar una segunda combinación distinta, sin repetir números de la primera
combinación2 = generar_combinación(combinación1)

# Generar una tercera combinación distinta, sin repetir números de la primera y segunda
combinación3 = generar_combinación(combinación1.union(combinación2))

# Convertir los conjuntos en cadenas y unir los elementos
cadena1 = " ".join(map(str, combinación1))
cadena2 = " ".join(map(str, combinación2))
cadena3 = " ".join(map(str, combinación3))

# Imprimir las combinaciones
print("Primera combinación:", cadena1)
print("Segunda combinación:", cadena2)
print("Tercera combinación:", cadena3)"""



import random

# Función para generar una combinación de 10 números aleatorios únicos entre 1 y 80
def generar_combinación():
    combinación = set()
    while len(combinación) < 10:
        combinación.add(random.randint(1, 80))
    return combinación

# Generar las tres combinaciones de 10 números aleatorios únicos
combinación1 = generar_combinación()
combinación2 = generar_combinación()
combinación3 = generar_combinación()

# Convertir las combinaciones en cadenas y unir los elementos
cadena1 = " ".join(map(str, combinación1))
cadena2 = " ".join(map(str, combinación2))
cadena3 = " ".join(map(str, combinación3))

# Imprimir las tres combinaciones
print("Primera combinación:", cadena1)
print("Segunda combinación:", cadena2)
print("Tercera combinación:", cadena3)
