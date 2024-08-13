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

import random

# Generar la primera combinación de 20 números aleatorios entre 1 y 80
combinación1 = [random.randint(1, 80) for _ in range(20)]

# Generar una segunda combinación distinta de 20 números aleatorios entre 1 y 80
combinación2 = [random.randint(1, 80) for _ in range(20)]

# Convertir las listas en cadenas y unir los elementos
cadena1 = " ".join(map(str, combinación1))
cadena2 = " ".join(map(str, combinación2))

# Imprimir las dos combinaciones
print("Primera combinación:", cadena1)
print("Segunda combinación:", cadena2)

