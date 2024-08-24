"""
Práctica en el aula Mod-6

Contador de Palabras

Escribe un programa que cuente el número de palabras en una frase ingresada por el usuario.
Considera que las palabras pueden estar separadas por espacios.

OJO: Debe tener un función llamada contar_palabras que reciba como
parámetro frase y que retorne el total de las palabras
"""

frase = input("Ingrese una Frase: ")

def contar_palabras(frase02):
    return len(frase02.split()) 

print(f'La Frase: "{frase}", Tiene {contar_palabras(frase)} palabras.')