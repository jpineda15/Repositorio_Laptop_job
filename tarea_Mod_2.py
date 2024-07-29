'''
Define una constate llamada PI con el valor
de 3.14159. Luego, solicita al usuario que ingrese el radio de un circulo.
Utilizando la constante PI, calcula el area del cirulo
(formula: area = PI * radio**2)
Imprime un mensaje que indique el area culculada 
'''
def area_PI(): # Creamos funcion 
    PI = 3.14159 # declaramos la constante PI
    radio = float(input("Ingrese el radio del circulo: ")) # Solicitamos al usuario ingresar el radio del círculo
    area = PI * radio**2 # calcula el área del círculo
    print("El area del circulo es: ", area) # Imprimimos el resultado 
area_PI() # Llamamos a la función
