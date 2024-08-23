# bucle (loops) for 
# for variable in elemento a recorrer (Sintaxis)
''''
for i in [1,2,3]:
    print("Hola Mundo")

for i in ["primavera","verano","otoño","invierno"]:
    print("Hello Python")

for i in ["primavera","verano","otoño","invierno"]:
    print(i)

for i in ["primavera","verano","otoño","invierno"]:
    print("Hello Python", end=" ")

for i in "hola":
    print("Hi Zabdiel")


# Validar correo 
def correo():
    email = False
    myEmail = input("Introduce tu direccion de Email: ")
    for i in myEmail:
        if (i == "@"):
            email = True
    if email:
        print("El Correo electrónico es correcto")
    else:
        print("El Correo electrónico no es correcto")
correo()
'''

def correo():
    contador = 0
    myEmail = input("Introduce tu direccion de Email: ")
    for i in myEmail:
        if (i == "@" or i == "."):
            contador = contador + 1
    if contador == 2:
        print("El Correo electrónico es correcto")
    else:
        print("El Correo electrónico no es correcto")
correo()


'''
# Ejemplo 01
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in lista:
    print(num)
print("Fin del proceso")

lista2 = ['Azul', 'Negro', 'Verde', 'Blanco', 'Rojo']
for color in lista2:
    print(color)
print("Fin del Proceso")

print("#####################################################")

for num2 in range(1, 12):
        print(num2)

#  bucle for que cuente desde el 1 hasta el 100
num = 100
for num2 in range(1, num + 1):
    if num2 <= num:
        print(num2)



print("#####################################################")

# Numeros pares 
num = 20
for n in range(1, num + 1):
    if n % 2 == 0:
        print(n)
        

print("#####################################################")
# Imprime los numero pares usando el bucle for. 

def num_par(num):
    for num2 in range(2, num + 1):
        if num2 % 2 == 0:
            print(num2)
    print("Fin del Ciclo")

valor = int(input("Ingresa un Valor: "))
num_par(valor)


print("#####################################################")


def num_par(num):
    for num2 in range(1, num + 1):
        if num2 % 2 == 0:
            print(num2)
    print("Fin del Ciclo")

valor = int(input("Ingresea un Valor: "))

num_par(valor)


# numero impares 
print("#####################################################")

num = 21
for n in range(1, num + 1):
    if n % 2 != 0:
        print(n)
print("Fin del Ciclo")



print("#####################################################")
# Funcion que imprima los numero impares 
def num_impa():
    num = 15
    for num2 in range(1, num + 1):
        if num2 % 2 != 0:
            print(num2)
    print("Fin del Ciclo")
num_impa()


print("#####################################################")

# Funcion que solicite por consola un numero y imprima los numeros que ahi del 1 al numero ingresado 
def num_impa():
    num = int(input("Ingresa un numero: "))
    for num2 in range(1, num + 1):
        if num2 % 2 != 0:
            print(num2)
    print("Fin del ciclo")

num_impa()


# conteo regresivo con for 
num = 5 
for n in range(num, 0, - 1):
    print(n)
print("Fin del Ciclo")



# Solicita un numero por consola y realizar un conteo decendiente
def decen_num():
    num = int(input("Ingrese un Valor: "))
    if num > 0:
        for n in range(num, -1, -1):
            print(n)
    else:
        print("Ingrese un Numero Positivo.")
    print("Fin del Ciclo")
decen_num()


# Tabla de Multiplicar 
def tabla_multiplicar():
    num = int(input("Ingrese un Numero: "))
    resul = 0
    for num2 in range(1, + 13):
        if num > 0:
            resul = num * num2
            print(f"{num} x {num2} = {resul}")
        else:
            print("Ingrese un Numero mayor que 0.")
    print("Fin del Ciclo")
tabla_multiplicar()


def numran2():
    import random 
    my_set = set()
    
    for i in range(1, 21):
        my_set.add(random.randint(1, 80))
    my_list = sorted(my_set)
    print(my_list)
numran2()
'''

