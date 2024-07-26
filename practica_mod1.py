'''
Desarrolle un programa en python que permita al usuario introducir 3 números de tipo decimal(foat),
el programa debe mostrar la sumatoria de los 3 números introducidos por el usuario.

    -En la primera línea agregue un comentario de una línea donde especifique el nombre de su programa.

    -Agregue un comentario de varias líneas donde describas el algoritmo (los pasos de dicho programa).

# Programa que solicita 3 valores al usuario y realiza una suma
def suma() -> None: # Declarar una función que contenga todo el código a utilizar.
    print()
    num_1 = float(input("Ingrese el Primer Valor: ")) # Solicitamos un primer valor por consola
    num_2 = float(input("Ingrese un Segundo Valor: ")) # Solicitamos un segundo valor por consola
    num_3 = float(input("Ingrese un Tercer Valor: ")) # Solicitamos un tercer valor por consola
    resul = (num_1 + num_2 + num_3) # Sumamos los 3 valores ingresados por el usuario
    print()
    print("La suma de ", '(',num_1, '+', num_2, '+', num_3,')', '=', resul) # Imprimimos el resultado de la suma.
    print()
suma() # Llamamos la función 
'''
# que es una constante en python
'''
Define una constate llamada PI con el valor
de 3.14159. Luego, solicita al usuario que ingrese el radio de un circulo.
Utilizando la constante PI, calcula el area del cirulo
(formula: area = PI * radio**2)
Imprime un mensaje que indique el area culculada
'''
def area_PI(): # Creamos funcion 
    PI = 3.14159
    radio = float(input("Ingrese el radio del circulo: "))
    area = PI * radio**2
    print("El area del circulo es: ", area)
area_PI()