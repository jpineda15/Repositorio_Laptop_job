from random import randint # Importamos la función randint del módulo random para generar números enteros aleatorios


"""
1) Generar Números Aleatorios:
    Crea una lista de 5 números enteros aleatorios entre 1 y 50.
"""
def numAle():
    num = [] # Lista vicia 
    for _ in range(5): # Iteramos 5 veces
        num.append(randint(1, 50)) # randint genera un numero entero entre 1 & 50.
    return num # Devuelve la lista después de completar todas las iteraciones.

"""
2) Mostrar la Lista: 
    Imprime la lista generada.
"""
numeroAleatorios = numAle()
print(f'Lista Generada: {numeroAleatorios}')

"""
3) Ordenar la Lista:
    Ordena la lista de menor a mayor utilizando la función sorted().
"""
print("Lista Ordenada: ",(sorted(numeroAleatorios)))

"""
4) Calcular la Media de los Valores:
    Calcula la media (promedio) de los valores en la lista e imprima."""
promedio = sum(numeroAleatorios)/5
print(f'El promedio de los valores de la lista es: {promedio}')


"""
5) Buscar un Número en la Lista:
    Solicita al usuario un número y verifica si ese número se encuentra en la lista.
    Informa al usuario si el número está o no en la lista."""
new_list = sorted(numAle())
num = int(input("Ingrese un numero del 1 al 50: "))
if num in new_list:
    print(f"El numero {num}, esta en la Lista: {new_list}")
else:
    print(f"El numero {num}, no esta en la Lista: {new_list}")


'''
6) Sumar los Valores de la Lista:
    Calcula la suma de todos los valores de la lista e imprima.'''
totalSum = sum(new_list)
print(f'Suma de los valores de la lista: {totalSum}')