### Metodos de str en Pythoy


# 1: capitalize()
text: str = 'hollo'
print(text.capitalize()) #  Convierte el primer carácter de la cadena en mayúscula.

# 2: casefold()
text: str = 'JuAn'
print(text.casefold()) # el contenido de la variable en minuscula

# 3: center()
text: str = 'hollo'
text2: str = "Hollo"
print(text.center(20)) # Centraliza el contenido de la variable
print(text2.center(20, '.'))

# 4: count()
text: str = 'abc_abc_abc'
print(text.count('ab')) # Contabiliza los caracteres almacenado

# 5: encode()
text: str = 'Juan Pineda'
print(text.encode(encoding='UTF-8', errors='strict'))

# 6: upper() --> Convierte todos los caracteres a mayúsculas.
text_6 = "hola mundo"
text_mayusculas = text_6.upper()
print(text_mayusculas)

# 7: lower() --> Nos permite transformar un texto a minúsculas.
text_7 = "HOLA MUNDO"
texto_minusculas = text_7.lower()
print(texto_minusculas)

print("#######################################################")
# 8: strip() --> nos permite eliminar los espacios innecesarios al inicio y al final de una cadena de texto.

# Escribe tu código aquí
def limpiar_texto(texto1, texto2):
    resul = texto1.strip() + texto2.strip()
    return resul
# Fin
print(limpiar_texto("  hola","  mundo"))
print(limpiar_texto("vaso   ","agua    "))
print(limpiar_texto("   sal   ","   pimienta "))

# Quitar espacio a una Lista
# Escribe tu código aquí
def limpiar_y_agregar(lista, nombre):
    lista_clear = [item.strip() for item in lista]
    nombre_clear = nombre.strip()
    lista_clear.append(nombre_clear)
    return lista_clear

# Fin
print(limpiar_y_agregar(["uno", "dos", "tres", "cuatro"], "       cinco"))
print(limpiar_y_agregar(["Camilo", "Ignacio", "Constanza"], "      Juana     "))
print(limpiar_y_agregar(["perro", "gato", "pájaro", "pez"], "    cabra   "))


print("#######################################################")

# 9: len() --> Podemos conocer la longitud de una cadena de texto utilizando la función len() de los strings
longitud = "hola Python"
print(len(longitud))

print("#######################################################")

# 10: slicing --> El método slicing es una técnica en programación que permite obtener una subsección de una lista, tupla, cadena de texto o cualquier estructura de datos que soporte indexación.

"""
Crea una función llamada largo_texto que reciba dos parámetros, texto1 y texto2.
La función debe retornar la suma de las longitudes de texto1 y texto2.
"""
# Escribe tu código aquí
def largo_texto(texto1, texto2):

    suma = len(texto1) + len(texto2)
    return suma 
# Fin
print(largo_texto("hola","mundo"))
print(largo_texto("día","noche"))
print(largo_texto("javascript","sqlite"))

# 10: slicing --> 

# Escribe tu código aquí
def primeros_caracteres(texto):
    return texto[0:3]
# Fin
print(primeros_caracteres("Hello"))
print(primeros_caracteres("Lenguaje"))
print(primeros_caracteres("Tutoriales"))

print("#######################################################")

"""
Crea una función llamada exceptoLosPrimeros que reciba dos parámetros:
texto y cantidad. La función debe retornar el texto sin los primeros caracteres, 
donde la cantidad de caracteres a omitir es el segundo parámetro.
"""
# Escribe tu código aquí 
def exceptoLosPrimeros(texto,cantidad):
    return texto[cantidad:]
# Fin 
print(exceptoLosPrimeros("Hola Mundo",6))
print(exceptoLosPrimeros("Programación en Javascript",8))
print(exceptoLosPrimeros("Tutoriales",3))

print("#######################################################")
"""
Crea una función que se llame encontrar_secreto que dependa de un parámetro de tipo string y 
devuelva un nuevo string con un salto de 2.
encontrar_secreto("2s1eecBr1eto") => "secreto"
"""
# Escribe tu código aquí 
def encontrar_secreto(string):
    return string[1::2]

# Fin 
print(encontrar_secreto("3t2e1s2t2i2n5g"))
print(encontrar_secreto("8m4y6s4e7c7r8e8t"))
print(encontrar_secreto("9h3i1d4d4e7n8m8e4s9s5a9g8e"))


print("#######################################################")
# 11: append() --> Podemos agregar un nuevo elemento a una lista utilizando el método append().

# Escribe tu código aquí
nombres = ["Juan", "Pedro", "Ana", "Luis"]
nombres.append("Maria")
print(nombres)  # ["Juan", "Pedro", "Ana", "Luis", "Maria"]

print("#######################################################")
""" 
12: pop() --> se usa para eliminar y devolver un elemento de una lista.
pop() sin argumentos elimina y devuelve el último elemento de la lista.
pop(index) elimina y devuelve el elemento en la posición especificada por index.
"""
frutas = ["manzana", "pera", "uva"]
ultima_fruta = frutas.pop()
print(ultima_fruta)  # "uva"
print(frutas)  # ["manzana", "pera"]

numeros = [10, 20, 30, 40]
segundo_numero = numeros.pop(1)
print(segundo_numero)  # 20
print(numeros)  # [10, 30, 40]

# Escribe tu código aquí
def eliminar_especial(números):
    if len(números) > 5:
        num = números.pop(5)
        return números
    elif len(números) == 5:
        num2 = números.pop(2)
        return números
    elif len(números) < 5:
        return números
# Fin
print(eliminar_especial([10, 20, 30, 40, 50, 60]))
print(eliminar_especial(["manzana", "pera", "uva", "naranja", "kiwi"]))
print(eliminar_especial([1, "dos", 3.0, "cuatro"]))