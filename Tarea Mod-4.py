"""
Crea una lista de frutas que contenga 10 elementos y por cada fruta imprime 
su nombre, pero también cuenta la cantidad de caracteres que tiene dicha fruta, 
utiliza un ciclo for y un ciclo while:
"""

def frutListW(): # Utilizamos el bucle while
    frutas = [
            'Mora', 'Cereza',
            'Naranja', 'Mango',
            'Pera', 'Kiwi',
            'Sandia', 'Papaya',
            'Carambola', 'Limón']
    i = 0
    while i < len(frutas):
        print(f"En nuestra lista tenemos: '{frutas[i]}' tiene '{len(frutas[i])}' Caracteres.")
        i += 1
frutListW()

print("###################################################")

def frutListF(): # Utilizamos el bucle for
    frutas = [
            'Mora', 'Cereza',
            'Naranja', 'Mango',
            'Pera', 'Kiwi',
            'Sandia', 'Papaya',
            'Carambola', 'Limón']
    for a in frutas:
        print(f"En nuestra lista tenemos: '{a}' tiene '{len(a)}' Caracteres.")
frutListF()