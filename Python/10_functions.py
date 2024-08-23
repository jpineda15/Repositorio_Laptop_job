### Functions ###
"""
def my_function(): # funcion simple
    print("Esto es una Function")

my_function()
my_function()

def sum_two_values(primer_valor, segundo_valor): # funcion que recibe parametros
    print(primer_valor + segundo_valor)

sum_two_values(4, 5)
sum_two_values(4.3, 5)
sum_two_values("Hola", "Mundo")

def funct01(primer_valor, segundo_valor):
    my_sum = primer_valor + segundo_valor
    return my_sum

my_result = funct01(1.4, 5.2)
print(my_result)

my_result01 = funct01(3.5, 3.5)
print(my_result01)


def print_name (name, surname):
    print(f"Hello, my name is {name} {surname}")

print_name(surname = "Pineda", name = "Juan Francisco")


def print_name_with_default (name, surname, alias = "Sin alias"): # Utilizando un valor por difor(en caso que no agreguen)
    print(f"Hello, my name is {name} {surname} and my alias is {alias}")

print_name_with_default("Juan Francisco", "Pineda Candelario", "Jpineda")
print_name_with_default("John Manuel", "Pineda De Jesus")


def print_texts(*texts):
    print(texts)

print_texts("Hello")
print_texts("Hi", "Python", "SQL")


def print_texts1(*txts):
    for text in txts:
        print(text)

print_texts1("Python", "Oracle", "GNU/Linux")

print("#############################################################################")

Crea una función llamada a_mayusculas que reciba dos parámetros, texto1 y texto2.
La función debe retornar un nuevo texto que sea la concatenación de texto1 y texto2 en mayúsculas, sin espacios adicionales entre ambos textos.
"""
'''# Escribe tu código aquí
def a_mayusculas(texto1, texto2):
    resul = texto1.upper() + texto2.upper()
    return resul

# Fin
print(a_mayusculas("hola", "mundo"))
print(a_mayusculas("cat", "Dog"))
print(a_mayusculas("King", "kong"))


# numero pares
def pares (num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
            '''
            

def suma(num1, num2)-> int:
    return num1 + num2
print(suma(2, 3)) #---> Imprimir el resultado de la función suma
print(type(suma(2,3))) #---> Tipo de archvio que devuelve.