### loops (blucles) ###

# 1- while

my_condition = 0
"""
while my_condition < 10: # Mientra sea verdadero se estara ejecutando. 
    print(my_condition)
    my_condition += 1
"""
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print(f"Mi condicion es {my_condition} Detener Loops.")
        break # Detine el loops
#print("Mi condicion es menor o igual que 20")



# 2- for

my_lists = (20, 30, 40, 50, 60)

for element in my_lists:
    print(element)


my_tuple = (35, 1.77, "Juan", 'Pineda')

for element in my_tuple:
    print(element)


my_set = {"Juan", "Pineda", "Python"}

for element in my_set:
    print(element)


my_dict = {
    "Nombre":"Juan",
    "Apellido":"Pineda",
    "Edad":"35",
    "Lenguaje": {"SQL", "Python", "Java"},
    1:1.30
    }

for element in my_dict.items():
    print(element)


for element in my_dict:
    print(element)
    if element == "Edad":
        break
print("El Loops For para el diccionario ha finalizado.")
