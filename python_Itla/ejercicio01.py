'''
Primera Funcion

def saluda(nombre:str) -> None:
    print(f'Hola, {nombre}')
    #print("Hello, " + nombre)
saluda("Juan")

def saludo_educador(nombre:str) -> None:
    saluda(nombre)
    print("Encantado de Conocerle.")
saludo_educador("Zabdiel")

# Operadores
print(4 > 5)
print(4 < 5 and 5 < 6)
print( 3 + 1 == 4)

def doble(x:float) -> float:
    return x * 2
print("Total es: ", doble(10))
print(doble(5))


def tex(nom:str) -> None:
    print("Helo," + nom)
n = tex("Juan")
print(n) #-> None = esta variable esta vacia no devuelve nada

def suma(x:float, a:float) -> float:
    return  x + a
print("Suma de x + a :", suma(3, 4))
s = suma(2,4)
print(type(s)) # --> Devuelve un numero entero


x = float(input("Ingrese el Nuevo Valor de X : "))
a = float(input("Ingrese el Nuevo Valor de A : "))

print("Nueva Suma de X + A = ", suma(x, a))
'''


def promedio() -> None:
    info = '''
    Evaluación del Estudiante. \n
    (Criterio de Evaluación)  
    1-> Asistencias y Participación: 15 
    2-> Foros: 2(2) = 4
    3-> Evaluación 2(3)= 6
    4-> Práctica en el aula: 9(2) = 18
    5-> Tareas: 9(3) = 27
    6-> Proyecto Final: 30
    '''
    print(info)
    print()
    nota_1 = int(input("Ingrese Nota de Asistencias y Participación: "))
    nota_2 = int(input("Ingrese Nota de Foros: "))
    nota_3 = int(input("Ingrese Nota de Evaluación: "))
    nota_4 = int(input("Ingrese Nota de Práctica en el aula: "))
    nota_5 = int(input("Ingrese Nota de Tareas: "))
    nota_6 = int(input("Ingrese Nota de Proyecto Final: "))
    prom = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5 + nota_6)
    prom2 = prom/6
    print("Nota Final:", prom)
    if prom >= 70:
        print("Aprobado")
        print(prom2)
    else:
        print("Reprobado")
        print(prom2)
promedio()