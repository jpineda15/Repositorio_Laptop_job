### List Comprehension(comprensiones de listas) ###
"""
# Lista normal
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

# list comprehension 
my_list = [i for i in my_original_list]
print(my_list)

my_new_list = [i for i in range(1, 21)] # lista que imprime del 1 al 20
print(my_new_list)

my_new_list = [i + 1 for i in range(21)] # lista que imprime del 1 al 21
print(my_new_list)

my_new_list = [i * 2 for i in range(1, 10)] # lista que imprimer el doble del 1 al 9
print(my_new_list)

my_new_list = [i * i for i in range(1, 10)] # lista que imprimer la multiplicacion de lo mismo numero
print(my_new_list)



def sum_five(num):
    return num + 5
my_new_list = [sum_five(i) for i in range(1, 10)]   # Lista que cuenta del 1 al 9 y lego la funcion sum_five le suma 5 a cada resultado
print(my_new_list) 
"""

## Resolucion de Ejercicios.  

