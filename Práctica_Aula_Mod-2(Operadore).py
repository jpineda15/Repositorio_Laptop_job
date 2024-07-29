# Práctica en el aula Mod-2
# Programa que realiza las diferentes operaciones como (+,-,*,/)

    # Declaramos la función operadores
def operadores():
        # Solicitamos la entrada de dos valores
    num_1 = int(input("Ingrese el Primer Valor: "))
    if num_1:
        num_2 = int(input("Ingrese el Segundo Valor: "))
        if num_2:
        # Realizamos las operaciones matemáticas correspondientes
            resul1 = num_1 + num_2
            resul2 = num_1 - num_2
            resul3 = num_1 * num_2
            resul4 = num_1 / num_2
            resul5 = num_1 // num_2
            resul6 = num_1 % num_2
            resul7 = num_1 ** num_2
        # Imprimimos los resultados de las distintas operaciones
            print(f"La Suma de {num_1} + {num_2} = {resul1}")
            print(f"La resta de {num_1} - {num_2} + {resul2}")
            print(f"La multiplicacion de {num_1} * {num_2} = {resul3}")
            print(f"La División de {num_1} / {num_2} = {resul4}")
            print(f"División Entera de {num_1} // {num_2} = {resul5}")
            print(f"El Módulo (resto de la división) de  {num_1} % {num_2} = {resul6}")
            print(f"La Exponenciación de {num_1} ** {num_2} = {resul7}")
        else:
            print(f"El segundo valor es 0")
    else:
        print(f"El primer valor es 0")

# Llamamos la función operadores
operadores()