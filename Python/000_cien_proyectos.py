""" ejercicios 1/100 """
"""
# 1. Sumar dos numeros y motrar su resultado

num: int = 2 + 5
print("1-) El resultado es:", num)

# 2. Calcula el area de un circulo con un radio dado 

import math # importa el módulo math, que proporciona acceso a funciones matemáticas avanzadas y a constantes matemáticas, como pi
radio: float = 5
area = math.pi * radio ** 2
print("2-) El area del circulo es:", area)

# 3. Concatena dos cadenas de texto

cadena1: str = "Hola"
cadena2: str = "Mundo"
print("3-) La concatenación es:", cadena1 + " " + cadena2)
concatenacion = cadena1 + " " + cadena2
print("3-) La concatenación es:", concatenacion)


# 4. Crear lista con diferentes elementos e imprimirla 

my_lists = ['Python', "Oracle", 'GNU/Linux', "Microsoft SQL Server"]
print(type(my_lists))
print(f"Mi lista de Aprendisaje es: {my_lists}")

my_other_lists = [1, "Dos", 3.5, True]
print("Elementos: ", my_other_lists)

"""

def restar(a, b, c):
    resultado = a - b - c
    print(f"El resultado de restar {a}, {b} y {c} es: {resultado}")

# Ejemplos de uso:
restar(10, 5, 2)  # Esto imprimirá: El resultado de restar 10, 5 y 2 es: 3
restar(20, 7, 3)  # Esto imprimirá: El resultado de restar 20, 7 y 3 es: 10
