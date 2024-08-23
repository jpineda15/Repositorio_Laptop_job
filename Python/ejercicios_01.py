#validar si el numero ingresado es par o impar

print('Numero Par o Impar')

num = int(input("Ingrese un Numero: "))

if num % 2 == 0:
    print("El numero es Par", num)
else:
    print("El numero es Impar", num)


"""
Crea una función llamada es_par que dependa de un parámetro numero.
Si el número es par, la función debe retornar el valor 1, si no, debe retornar el valor 0.
"""

# Escribe tu código aquí
def es_par(numero):
    if numero % 2 == 0:
        return 1
    else:
        return 0

# Fin
print(es_par(4))
print(es_par(5))
print(es_par(1))


"""
Crea una función llamada esDivisible que dependa de dos parámetros:numero y divisor.
Si el número es divisible por el divisor, la función debe retornar el valor 1, si no, debe retornar el valor 0.
"""
def es_Divisible(numero, divisor):
    if numero % divisor == 0:
        return 1
    else:
        return 0
print(es_Divisible(10,5))
print(es_Divisible(10,3))
print(es_Divisible(10,2))



def es_python(language):
    if language == "Python":
        return 1
    else:
        return 0

# Ejemplos de uso
print(es_python("Python"))  # Esto imprimirá 1
print(es_python('Java'))    # Esto imprimirá 0

def es_python(language):
    if language == "Python":
        print('Este proyecto no utiliza Python.')
    else:
        print('Este proyecto utiliza Python.')

# Ejemplos de uso
es_python("Python")
es_python("Java")



def adivinaNumero(numero):
    if numero == 7:
        return "Adivinaste el número secreto"
    elif numero == 6:
        return "Casi, pero no es el número secreto"
    else:
        return "Estás equivocado, el número secreto no es {}".format(numero)

# Ejemplos de uso
print(adivinaNumero(7))  # Esto imprimirá "Adivinaste el número secreto"
print(adivinaNumero(8))  # Esto imprimirá "Estás equivocado, el número secreto no es 8"
print(adivinaNumero(6))  # Esto imprimirá "Casi, pero no es el número secreto"



# Escribe tu código aquí
language = 'Python'

if language == 'Python':
    print('Este proyecto utiliza Python.')
else:
    print('Este proyecto no utiliza Python.')

# Fin

print("###################################################")

"""
Utilizando lo aprendido en ejercicios anteriores, 
crea una función llamada obtener_dia que permita obtener el nombre correspondiente 
al día de la semana a partir del parámetro día.
El valor pasado será un número del 0 al 6 que representa el día de la semana. Si el día es 0, 
la función debe retornar "Domingo". Si el día es 1, la función debe retornar "Lunes",
y así sucesivamente hasta el día 6 que corresponde a "Sábado".
Si el día es cualquier otro valor, la función debe retornar "Valor inválido".
"""

def obtener_dia(nombre):
    if nombre == 0:
        return "Domingo"
    elif nombre == 1:
        return "Lunes"
    elif nombre == 2:
        return "Martes"
    elif nombre == 3:
        return "Miercoles"
    elif nombre == 4:
        return "Jueves"
    elif nombre == 5:
        return "Viernes"
    elif nombre == 6:
        return "Sábado"
    else:
        return "Valor inválido"
print(obtener_dia(1))
print(obtener_dia(2))
print(obtener_dia(6))
print(obtener_dia(9))


# ifs anidados
print("###################################################")
# Escribe tu código aquí

def revisarAntesDeSalir(llaves, celular):
# Convertir las cadenas 'Si' y 'No' a booleanos
    llaves = llaves.lower() == 'si' # convertir a booleanos
    celular = celular.lower() == 'si' # convertir a booleanos
# ifs anidados
    if llaves == True:
        if celular == True:
            return "Todo listo, puedes salir de casa"
        else:
            return "Te falta el celular"
    else:
        return "Te falta las llaves"

# Fin
print(revisarAntesDeSalir('Si', 'Si'))
print(revisarAntesDeSalir('Si', 'No'))
print(revisarAntesDeSalir('No', 'Si'))
print(revisarAntesDeSalir('No', 'No'))


print("#######################################################")

# Escribe tu código aquí

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
