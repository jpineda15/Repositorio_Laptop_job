'''
Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” 
encargada de devolver el número más alto de los dos introducidos.
'''
"""
def devuelveMax():
    num_1 = int(input("Ingrese un Primer Valor: "))
    num_2 = int(input("Ingrese un Segundo Valor: "))
    if num_1 > num_2:
        print("El numero", num_1 ,"es Mayor que", num_2)
    elif num_2 > num_1:
        print("El numero", num_2,"es Mayor que", num_1)
    else:
        print("Los dos Valores ingresado son iguales: ", num_1,"|", num_2)
    print("Fin del Programa")
devuelveMax()
"""

'''
Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”.
Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje:
“Los datos personales son: nombre Dirección teléfono” (Se mostrarán los datos introducidos por teclado).
'''
"""
def datosperson():
    datos = list()
    nom = input("Ingrese el Nombre: ")
    datos.append(nom)
    direc = input("Ingrese su Dirección: ")
    datos.append(direc)
    tel = input("Ingrese su numero de Teléfono: ")
    datos.append(tel)
    print("Los datos personales son: ",datos)
datosperson()
"""

# Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos.
def mediaAritme():
    num_1 = int(input("Ingrese un Primer Valor: "))
    num_2 = int(input("Ingrese un Segundo Valor: "))
    num_3 = int(input("Ingrese un Tercer Valor: "))
    media = (num_1 + num_2 + num_3) / 3
    print("La media aritmética de los tres numeros es: ", media)
mediaAritme()