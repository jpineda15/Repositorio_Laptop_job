# Bucle for --> continue
'''for lentra in "Python":
    if lentra == "h": 
        continue # cuendo la condicion se cumpla, no se imprimira la letra "h"
    print(f"Viendo la letra: {lentra}")'''

# Ejemplo con continue
def espacioEnblanco():
    texto = "Hola, soy un texto con espacio en blanco"
    contador = 0
    
    for letra in texto:
        if letra == " ":
            continue # Cuando se cumpla la condicion NO contara los espacio en blanco. 
        contador += 1
    print(contador)
espacioEnblanco()

# Bucle for --> break
'''for ver in "Adriel":
    if ver == "e":
        break # cuando la condicion se cumpla el bucle termina
    print(f"Viendo la letra: {ver}")'''