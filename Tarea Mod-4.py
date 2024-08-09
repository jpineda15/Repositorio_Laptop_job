"""
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
        print(f"En nuestra lista tenemos: '{frutas[i]}' y tiene '{len(frutas[i])}' Caracteres.")
        i += 1
frutListW()

def frutListF(): # Utilizamos el bucle for
    frutas = [
            'Mora', 'Cereza',
            'Naranja', 'Mango',
            'Pera', 'Kiwi',
            'Sandia', 'Papaya',
            'Carambola', 'Limón']
    for a in frutas:
        print(f"En nuestra lista tenemos: '{a}' y tiene '{len(a)}' Caracteres.")
frutListF()