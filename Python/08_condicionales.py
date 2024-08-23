### Condicionales 
"""
        Estructurade Control de Flujo
            1. Condicionales: if, elif, else
            2. Ciclos o Bucles: for , while
                1. break : termina el bucle actual
                2. continue: salta al inicio del bucle actual
                3. pass: no hace nada

my_condition = True

if my_condition:
    print("Se ejecuto el Primer if <---")
print("La ejecucion continua")

##

my_condition02 = False

if my_condition02:
    print("Se ejecuto el segundo if <---")
print("La ejecucion continua")

my_condition03 = 3 * 2

if my_condition03 == 6:
    print("Es igual a 6 <---")
print("La ejecucion continua")


if my_condition03 == 8:
    print("Es igual a 8 <---")
print("La ejecucion continua")

if my_condition03 > 6:
    print("Es Mayor que 6 <---")
print("La ejecucion continua")

#### Condition if else
if my_condition03 > 6:
    print("Es Mayor que 6 <---")
else:
    print("No es Mayor que 6 <---")


###
my_condition04 = 5 * 2

if my_condition04 > 10 and my_condition04 < 25:
    print("Es menor o igual que 10 o mayor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

###
my_condition05 = 5 * 3
if my_condition05 > 10 and my_condition05 < 25:
    print("Es Mayor que 10 y Menor que 25 ")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

####
my_condition06 = 5 * 5

if my_condition06 > 10 and my_condition06 < 20:
    print("Es Mayor que 10 o Menor que 25 ")
elif my_condition06 == 25:
    print("Es igual a 25")
else:
    print("No es Mayor que 10 o Menor que 25")


my_string = ''

if my_string:
    print("La cadena no esta vacia")
else:
    print("La cadena esta vacia")
"""
# Operador IN  | lower() --> traforma texto a minucula | upper() --> traforma texto a mayuscula
print(" Asignaturas Optativas 2024")
print("Asignaturas Optativas: Informatica Grafica - Pruebas de Software - Usabilidad & Accesibilidad")
opcion = input("Escribe la Asignatura Escogida: ")
asignatura = opcion.lower() # ---> convertir el contenido de la variable a minucula
if asignatura in ("informatica Grafica", "pruebas de software", "usabilidad & accesibilidad"):
    print("La Asignatura Escogida es: " + asignatura)
else:
    print("La Asignatura Escogida no es correcta")