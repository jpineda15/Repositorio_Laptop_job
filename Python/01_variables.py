""" Variables """

VARIABLES = "My String variable"
print(VARIABLES)

int_variable = 5
print(int_variable)

bool_variable = True
print(bool_variable)

# Algunas Funcione del Sistema 
print(len(VARIABLES))

# Variables en una sola Linea
nombre, apellido, alias, años = "Juan", "Pineda", "John", 35
print(nombre, apellido, alias, años)

# uso de "input"
name = input ("¿Cual es tu Nombre? ") 
age = input ("¿Cuantos años tines? ")

print(name)
print(age)


print("########################")





numero = int(input("Ingrese un valor"))  # Ejemplo de número
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
