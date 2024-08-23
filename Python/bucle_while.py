# Usando while
"""
Con while podemos repetir un bloque de código mientras una condición sea verdadera.
Es importante asegurarse de que la condición del while eventualmente se vuelva falsa para evitar bucles infinitos.
"""
# Ejemplo 1

'''
contador = 1
while contador <= 10:
    print(contador)
    contador += 1  # Incrementamos el contador en 1
print("Fin del ciclo")

print("##############################################################################################")
# Ejemplo 2
def contar_hasta(num):
    num2 = 1
    while num2 <= num:
        print(num2)
        num2 += 1
    print("Fin del Ciclo")
contar_hasta(4)
contar_hasta(12)
contar_hasta(7)
print("##############################################################################################")

# Escribir codigo aqui 
def desde_hasta(num, num2):
    while num <= num2:
        print(num)
        num += 1
    print("Fin del Ciclo")
# Fin 
desde_hasta(3,7)
desde_hasta(15,21)
desde_hasta(8,13)

print("##############################################################################################")

# Sumando con while
contador = 1
suma = 0
while (contador <= 10):
    suma = suma + contador
    contador = contador + 1
print(suma)

print("##############################################################################################")
"""
Crea una función llamada sumarHasta que reciba un número como parámetro.
La función debe retornar la suma de los números del 1 al número ingresado.
Por ejemplo, si el número ingresado es 5, la función debe retornar 15. Si el número ingresado es 10, la función debe retornar 55.
"""
# Escribe tu código aquí
def sumarHasta(num):
    suma = 0
    contador = 1
    while contador <= num:
        suma += contador
        contador += 1
    return suma
# Fin
print(sumarHasta(4))
print(sumarHasta(11))
print(sumarHasta(2))

print("##############################################################################################")
 
# Escribe tu código aquí
def sumarDesdeHasta(num, num2):
    suma = 0 
    while num <= num2:
        suma += num
        num += 1
    return suma
print(sumarDesdeHasta(4,9))
print(sumarDesdeHasta(2,5))
print(sumarDesdeHasta(50,136))

print("##############################################################################################")

"""
Crea una función llamada sumarDeDosEnDos que reciba dos parámetros, desde y hasta.
La función debe retornar la suma de los números.
"""

# Escribe tu código aquí 
def sumarDeDosEnDos(desde, hasta):
    suma = 0
    while desde <= hasta:
        suma += desde
        desde += 2
    return suma
# Fin
print(sumarDeDosEnDos(4,9))
print(sumarDeDosEnDos(2,5))
print(sumarDeDosEnDos(25,67))

print("##############################################################################################")

"""
Crea una función llamada productoria que reciba un número como parámetro y 
retorne la productoria de los números del 1 al número ingresado.
Por ejemplo, si el número ingresado es 5, la función debe retornar 120. 
Si el número ingresado es 10, la función debe retornar 3628800.
"""

# Escribe tu código aquí 
def productoria(num):
    num2 = 1
    produc = 1
    while num2 <= num:
        produc *= num2
        num2 += 1
    return produc
# Fin
print(productoria(9))
print(productoria(12))
print(productoria(7))





# Numero pares con while 

num = 100
num2 = 1
while num2 <= num:
    if num2 % 2 == 0:
        print(num2)
    num2 += 1
print("Fin del Ciclo")

print("##############################################################################################")



# Numeros Impares con while
num = 100
num2 = 1
while num2 <= num:
    if num2 % 2 != 0:
        print(num2)
    num2 += 1
print("Fin del Ciclo")

print("##############################################################################################")


def num_impar():
    num = int(input("Ingrese un Valor: "))
    num2 = 1
    while num2 <= num:
        if num2 % 2 != 0:
            print(num2)
        num2 += 1
    print("Fin del ciclo")
num_impar()

print("##############################################################################################")



def num_impar():
    num = int(input("Ingrese un Valor: "))
    num2 = 1
    while num2 <= num:
        if num2 % 2 != 0:
            print(num2)
        num2 += 1
    print("Fin del ciclo")

num_impar()

# Bucle while que cuenta desde el 1 al 100
num = 100
num2 = 1
while num2 <= num:
    print(num2)
    num2 += 1
print("Fin del Ciclo")

# Bucle while que cuenta desde el 1 al 100 (Funcion)
def contar_num():
    num = int(input("Ingrese un Valor: "))
    num2 = 1
    while num2 <= num:
        print(num2)
        num2 += 1
    print("Fin del Ciclo")
contar_num()

# Bucle while que cuenta desde el 100 al 1 
num = 100
while num >= 1:
    print(num)
    num -= 1
print("Fin del Ciclo")



# Bucle while que cuenta decendente el numero ingresado que sea mayor 0 hasta 1 (funcion)
def contar_num():
    num = int(input("Ingrese un Valor: "))
    if num > 0:
        while num >= 1:
            print(num)
            num -= 1
    else:
        print("Ingrese un Valor Mayor 0")
    print("Fin del Ciclo")
contar_num()


# Tabla de Multiplicar 
def tab_multi():
    num = int(input("Ingrese un Valor: "))
    num2 = 1
    resul = 0
    while num2 <= 12:
        if num > 0:
            resul = num * num2
            print(num, "x", num2, "=", resul)
            num2 += 1
        else:
            print("Ingrese un Valor Mayor 0")
    print("Fin del Proceso.")
tab_multi()


def validarEdad():
    edad = int(input("Introduce tu edad por favor: "))
    
    while edad < 5 or edad > 100:
        print(f"La edad introducida no es válida, por favor introduce una edad entre 5 & 100")
        edad = int(input("Introduce tu edad por favor: "))
    print(f"Gracias por colaborar. Puedes pasar")
    print(f"Edad del aspirante {edad}")
validarEdad()
'''

def raizCuadrada(): 
    import math  # Importamos la biblioteca math, que contiene funciones matemáticas, incluyendo sqrt para calcular la raíz cuadrada.
    print()
    print("Calcular la Raiz Cuadrada de un Numero")
    print()
    
    num_1 = int(input("Ingrese un Valor, por favor: "))  # Solicitamos al usuario que ingrese un número.
    intentos = 0  # Inicializamos una variable para contar los intentos del usuario.
    
    while num_1 <= 0:  # Mientras el número ingresado sea menor o igual a 0, el bucle continuará.
        print("Error, el valor ingresado debe ser mayor a 0")
        
        if intentos == 2:  # Si el usuario ha hecho 2 intentos incorrectos, se cierra el programa.
            print("Se han agotado los intentos, el programa se cerrará")
            break  # Salimos del bucle while.
        
        num_1 = int(input("Ingrese un Valor, por favor: "))  # Solicitamos nuevamente un número.
        
        if num_1 <= 0:
            intentos += 1  # Incrementamos el contador de intentos.
    
    if intentos < 2:  # Si el usuario ingresó un valor válido antes de agotar los intentos.
        solucion = math.sqrt(num_1)  # Calculamos la raíz cuadrada del número ingresado.
        print(f"La raiz cuadrada de {num_1} es: {solucion}")
        print("Fin del Proceso.")

raizCuadrada()  # Llamamos a la función para que se ejecute.
