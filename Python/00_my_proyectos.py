# Calculardora
"""
text1: str = "Calculadora"
print(text1.center(20, '.'))

num1 = input("Ingrese un Primer Valor: ")
num2 = input("Ingrese un Segundo Valor: ")

num1 = int (num1)
num2 = int (num2)

suma: int= num1 + num2
resta: int = num1 - num2
multiplicacion: int = num1 * num2
division: int = num1 / num2

operacion_dic = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division
}

print("Operaciones Disponibles: suma, resta, multiplicacion, division")
calcular: str = input("Ingrese el Nombre de la Operacion a realizar: ")

if calcular in operacion_dic:
    print(f"El resultado de la {calcular} es: {operacion_dic [calcular]}")
else:
    print("Operacion no disponible")
"""


def media(num_1, num_2, num_3):
    """
    Esta función toma tres números y retorna su media.
    """
    resul = num_1 + num_2 + num_3
    resul = resul / 3
    return resul

# Solicitar las tres notas al usuario
try:
    num_1 = float(input("Ingrese la Primera Nota: "))
    num_2 = float(input("Ingrese la Segunda Nota: "))
    num_3 = float(input("Ingrese la Tercera Nota: "))
    
    # Calcular la media usando la función
    resultado = media(num_1, num_2, num_3)
    
    # Mostrar el resultado
    print(f"La media de las tres notas es: {resultado}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
