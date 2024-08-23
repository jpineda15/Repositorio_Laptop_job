"""
Se necesita crear un sistema de descuentos según la cantidad de productos comprados y la hora del día.

Crea una función llamada descuentos que dependa de los parámetros cantidad y hora. La función debe retornar el descuento, que corresponderá al mensaje entregado para cada caso. Escribe un conjunto de "if" anidados para determinar la categoría de descuento basada en la cantidad de productos comprados y la hora del día:

"Mañana" y cantidad mayor o igual a 10: "Descuento del 25% en la compra matutina."
"Mañana" y cantidad mayor o igual a 5 pero menor que 10: "Descuento del 15% en la compra matutina."
"Mañana" y cantidad menor que 3: "Sin descuento en la compra matutina."
"Noche" y cantidad mayor o igual a 10: "Descuento del 15% en la compra nocturna."
"Noche" y cantidad mayor o igual a 5 pero menor que 10: "Descuento del 5% en la compra nocturna."
"Noche" y cantidad mayor o igual a 3 pero menor que 5: "Descuento del 3% en la compra nocturna."
"Noche" y cantidad menor que 3: "Sin descuento en la compra nocturna."

"""

def descuentos(cantidad, hora):
    if hora == "Mañana":
        if cantidad >= 10:
            return "Descuento del 25% en la compra matutina."
        elif cantidad >= 5 and cantidad <= 10:
            return "Descuento del 15% en la compra matutina."
        elif cantidad < 3:
            return "Sin descuento en la compra matutina."
    elif hora == "Noche":
        if cantidad >= 10:
            return "Descuento del 15% en la compra nocturna."
        elif cantidad >= 5 and cantidad <= 10:
            return "Descuento del 5% en la compra nocturna."
        elif cantidad >= 3 and cantidad < 5:
            return "Descuento del 3% en la compra nocturna."
        elif cantidad < 3:
            return "Sin descuento en la compra nocturna."
    else:
        return "Hora no valida."
# Fin
print(descuentos(15, 'Mañana'))
print(descuentos(2, 'Mañana'))
print(descuentos(5, 'Noche'))
print(descuentos(4, 'Noche'))



"""
Se busca hacer un asistente que te ayude a revisar todo lo que tienes que llevar antes de salir de casa. 
Para esto, se te pide crear una función que se llame revisar_antes_de_salir que depende de dos parámetros llaves y celular.

Si tienes las llaves y el celular, la función debe retornar "Todo listo, puedes salir de casa".
Si tienes solo las llaves, la función debe retornar "Te falta el celular".
Si no tienes las llaves, la función debe retornar "Te falta las llaves".
Los valores que pueden tomar llaves y celular son True o False, donde True significa que tienes el objeto y False que no lo tienes.
No se pide considerar otros valores.
"""


print("#########################################################################################################")

# Escribe tu código aquí
def revisar_antes_de_salir(llaves, celular):
    if llaves == True:
        if celular == True:
            return "Todo listo, puedes salir de casa"
        elif celular == False:
            return "Te falta el celular"
    else:
        return "Te falta las llaves"

# Fin
print(revisar_antes_de_salir(True, True))
print(revisar_antes_de_salir(True, False))
print(revisar_antes_de_salir(False, True))
print(revisar_antes_de_salir(False, False))



def llevarLaContraria(expresion):
    if expresion == True:
        return ( not expresion)
    else:
        return (not expresion)
    # Fin
print(llevarLaContraria(True))
print(llevarLaContraria(False))

print("#############################################################")

"""
Se pide crear una función llamada revisar_edad que dependa de un parámetro edad.
La función debe retornar "Realizar examen" si la edad es mayor que 40 y menor que 50.
En caso contrario, la función debe retornar "No realizar examen".
"""

# Escribe tu codigo aqui 
def revisar_edad (edad):
    if edad > 40 and edad < 50:
        return "Realizar examen"
    else:
        return "No realizar examen"
# Fin
print(revisar_edad(45))
print(revisar_edad(60))
print(revisar_edad(30))

print("#############################################################")
"""
FizzBuzz es un problema clásico de programación que consiste en mostrar una lista de 
números cuando cumplen ciertas condiciones.
En este ejercicio deberás crear la función fizz_buzz que depende de un parámetro numero. 
La función debe retornar:
"Fizz" si el número es divisible por 3.
"Buzz" si el número es divisible por 5.
"FizzBuzz" si el número es divisible por 3 y 5.
En caso de que el número no sea divisible por 3 o 5, debe devolver el mismo número.
"""
# Escribe tu código aquí
def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 5 == 0:
        return "Buzz"
    elif numero % 3 == 0:
        return "Fizz"
    else:
        return numero
# Fin
print(fizz_buzz(9))
print(fizz_buzz(25))
print(fizz_buzz(15))
print(fizz_buzz(4))

print("#############################################################")

"""
Crea una función llamada verificar_puntaje que dependa de un parámetro puntaje.
La función debe retornar "Califica para bono" si el puntaje es mayor que 90 o menor que 10. 
En caso contrario, la función debe retornar "No califica para bono".
"""
# Escribe tu código aquí
def verificar_puntaje(puntaje):
    if puntaje > 90 or puntaje < 10:
        return "Califica para bono"
    else:
        return "No califica para bono"
# Fin
print(verificar_puntaje(91))
print(verificar_puntaje(6))
print(verificar_puntaje(40))

print("#############################################################")

"""
Crea una función llamada mayorQue que dependa de dos parámetros : a y b

Si a es mayor que b, la función debe retornar "El primer número es mayor que el segundo"
Si b es mayor que a, la función debe retornar "El segundo número es mayor que el primero"
Si ambos números son iguales, la función debe retornar "Ambos números son iguales"
"""

# Escribe tu código aquí 
def mayorQue(a, b):
    if a > b:
        return "El primer número es mayor que el segundo"
    elif b > a:
        return "El segundo número es mayor que el primero"
    elif a == b:
        return "Ambos números son iguales"
# Fin 
print(mayorQue(3,5))
print(mayorQue(6,3))
print(mayorQue(5,5))

print("#############################################################")
"""
Crea una función llamada mayorDeTres que dependa de tres parámetros: a, b y c.

Si a es mayor que b y c, la función debe retornar "El primer número es el mayor"
Si b es mayor que a y c, la función debe retornar "El segundo número es el mayor"
Si c es mayor que a y b, la función debe retornar "El tercer número es el mayor"
Si los tres números son iguales, la función debe retornar "Los tres números son iguales"
"""
# Escribe tu código aquí 
def mayorDeTres(a, b, c):
    if a > b and a > c:
        return "El primer número es el mayor"
    elif b > a and b > c:
        return "El segundo número es el mayor"
    elif c > a and c > b:
        return "El tercer número es el mayor"
    elif a == b and b == c:
        return "Los tres números son iguales"
# Fin 
print(mayorDeTres(4,3,2))
print(mayorDeTres(5,6,1))
print(mayorDeTres(9,8,10))
print(mayorDeTres(7,7,7))
