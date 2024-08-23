### SETS o Conjunto(Estructura de Datos)  ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Juan","Pineda",35}
print(type(my_other_set))
print(my_other_set)
print(len(my_other_set))

my_other_set.add("Jpineda") # Agregar datos al set
print(my_other_set) # Un set no es una estrutura de datos ordenada.

my_other_set.add("Jpineda") # Agregar datos al set
print(my_other_set) # No permite datos repetidos

### Convertir set en list
my_set = {"Juan", "Pineda", "35"}
my_list = list(my_set)
print(type(my_set))
print(type(my_list))
print(my_list)
print(my_list[0])

my_other_set = {"Juan", "Pineda", "Python"}
my_new_set = my_set.union(my_other_set) ## Unir dos sets
print(my_new_set)
