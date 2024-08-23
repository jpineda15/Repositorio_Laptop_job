# Tipos Booleanos (bool) en Python.
# True y False
# True = Verdadero
# False = Falso

verda = True
falso = False
print(verda, falso)
print(type(verda))
print(type(falso))

falso = 3 > 2
print(falso)

if falso:
    print("Es falso")
else:
    print("Es verdadero")

print("############################################################")

# Procesar Entrada Datos en Python
# input() -> Recibe datos de entrada del usuario
# input() -> regresa yb tuoi de dato String(str)
resultado = input("Ingrese su Nombre: ")
print("Hola", resultado)

print("############################################################")

# Escribir codigo aqui
num1 = int(input("Ingrese un Primer valor: "))
num2 = int(input("Ingrese un Segundo valor: "))

#print("La suma es: ", int(num1) + int(num2))
suma = num1 + num2

print("La suma de ", num1, "y", num2, "es ", suma)

print("############################################################")

# Califica tu dia del 1 al 10
dia = int(input("Como estuvo tu dia (1 al 10): "))
print("Mi dia estuvo de:", dia)

print("############################################################")

"""
Se solicita incluir la siguiente informacion acerca de un Libro:
Titulo
Autor
Debes imprimir la informacion en el siguiente formato:
Proporciona el titulo:
Proporciona el autor:
<Titulo> Fue escrito por <Autor>
"""
titulo = input("Proporciona el titulo: ")
autor = input("Proporciona el autor: ")
print(titulo, "Fue escrito por", autor)

