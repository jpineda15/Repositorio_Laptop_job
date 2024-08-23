'''  # 1 Famoso "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
        Múltiplos de 3 por la palabra "fizz".
        Múltiplos de 5 por la palabra "buzz".
        Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


# Bucle For
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    else:
        print(n)

# Bucle while
num = 1
while num < 101:
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    num += 1
'''

"""
 #2 ANAGRAMA
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * -> Un Anagrama consiste en formar una palabra reordenando TODAS
 * -> las letras de otra palabra inicial.
 * -> NO hace falta comprobar que ambas palabras existan.
 * -> Dos palabras exactamente iguales no son anagrama.

def anagra(a, b):
    if len(a) == len(b):
        return sorted(a) == sorted(b)
    else:
        return False
print(anagra('hola', 'amor'))  # Esto imprimirá False
print(anagra('amor', 'roma'))  # Esto imprimirá True
print(anagra('anagrama', 'nagaram')) 
print(anagra('loco', 'hola'))
"""


"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

"""def fibo ():
    num = 50
    my_list = [0, 1]
    for i in range(2, num):
        num = my_list[i - 1] + my_list[i - 2]
        my_list.append(num)
    for num2 in my_list:
        print(num2)
fibo()
"""

def fibo2():
    other_list = [0, 1]
    for a in range(0, 51):
        nu = other_list[a - 1] + other_list[a - 2]
        other_list.append(nu)
    for num2 in other_list:
        print(num2)
fibo2()


'''Fibonacci'''
def fibo():
    n = 10
    a, b = 0,1
    for _ in range(n):
        yield a 
        a, b = b, a + b
print(list(fibo()))
