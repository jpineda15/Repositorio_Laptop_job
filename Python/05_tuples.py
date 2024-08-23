### TUPLES(Estructura de Datos) ###
#Tuplas: Son listas inmutables(que no cambia), es decir, no se pueden modificar despues de su creacion

'''my_tuple = tuple() # definiendo una tuple.
my_other_tuple = () # definiendo una tuple.

my_tuple = (35, 1.77, "Juan", 'Pineda')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[-2])
print(my_tuple[-4])

my_other_tuple = (15, 20, 25, 30)
print(my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # Convertir una tuples en list.
print(type(my_tuple))'''

myTupla =  ("Pedro", "Juan", "Maria", 20, 30, 40)
print(myTupla)
print(myTupla[3])
print(myTupla[0:4])
print('Juan' in myTupla) # --> Validar si existe el elemento en la tupla
print(myTupla.count(20)) # --> Contar las cantidad de veses que existe un elemento en la Tupla
print(len(myTupla)) # --> Cuenta la logitud o lemento de la tupla