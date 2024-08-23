'''### Lista(Estructura de Datos) ###

my_list = list() # declarando una lista.
my_other_list = [] # declarando una lista.

print(len(my_list))

my_list = [20, 24, 35, 40, 50, 20]
print(my_list)
print(len(my_list))

my_other_list = [24, 5, 40, "Juan", 'Pineda']
print(type(my_other_list))

print(my_other_list[0]) # selecionar un resultado de la lista.
print(my_other_list[1]) # selecionar un resultado de la lista.
print(my_other_list[-1]) # selecionar un resultado de la lista.
print(my_other_list[-3]) # selecionar un resultado de la lista.
print(my_list.count(20))

a, b, c, d, e, f = my_list #decempaquetando lista.
print(a)

print(my_list + my_other_list) #concatenar lista.

my_other_list.append("JFPTech") # Agrega elemento a la lista.
print(my_other_list)

my_other_list.insert(1, "Negro") #colocamos la posion donde queremos insertar el contenido agregado.
print(my_other_list)

my_other_list.remove("Negro") # Elimina articulo de la lista.
print(my_other_list)

print("#######################################################")
"""
Crea una función llamada primer_elemento que reciba una lista y retorne el primer elemento de cada lista.
"""
# Escribe tu código aquí
def primer_elemento(my_list):
    return my_list[0]
# Fin
print(primer_elemento([3, 4, 1, 5]))
print(primer_elemento(["e", "t", "r"]))
print(primer_elemento(["ruby", "javascript", "python"]))

print("#######################################################")

"""
Crea una función llamada obtener_subcadena que reciba como parámetro una lista de strings y
devuelva una nueva lista con los elementos en las posiciones pares (0, 2, 4, etc.) de la lista original.
"""
# Escribe tu código aquí
def obtener_subcadena(my_list2):
    return my_list2[::2]
# Fin
print(obtener_subcadena(["manzana", "pera", "uva", "naranja", "kiwi", "mango"]))
print(obtener_subcadena(["rojo", "azul", "verde", "amarillo", "negro", "blanco"]))
print(obtener_subcadena(["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]))

print("#######################################################")

"""
Crea una función llamada largo_lista que reciba un parámetro llamado nombres.
La función debe retornar el texto "muchos" si hay más de 5 elementos en la lista,
en caso contrario debe retornar "pocos".
"""

# Escribe tu código aquí
def largo_lista(nombres):
    resul = len(nombres)
    if resul >= 5:
        return "muchos"
    elif resul < 5:
        return "pocos"
# Fin
print(largo_lista([3, 4, 1, 5]))
print(largo_lista(["e", "t", "r"]))
print(largo_lista(["ruby", "javascript", "python", "c", "c#", "java"]))

print("#######################################################")
"""
Crea una función llamada ultimo_y_primero que reciba una lista y retorne la concatenación del último y 
el primer elemento de la lista.
"""
# Escribe tu código aquí : len()
def ultimo_y_primero(lista):
    listar = lista[-1] + lista[0]
    return listar
# Fin
print(ultimo_y_primero(["perro", "gato", "delfin", "tortuga"]))
print(ultimo_y_primero(["e", "t", "r", "z"]))
print(ultimo_y_primero(["ruby", "javascript", "python", "c", "c#", "java"]))



def agregar_si(lista):
    contar = len(lista)
    if contar < 5:
        lista.append("")
        if lista:
            return lista
    else:
        return "El Largo de la Lista es mayor que 5"

# Fin
print(agregar_si(["perro", "gato", "delfin", "tortuga"]))
print(agregar_si(["Francisco", "Rene", "Gonzalo", "Consuelo"]))
print(agregar_si(["ruby", "javascript", "python", "c", "c#", "java"]))



def agregar_si(lista, elemento):
    contar = len(lista)
    if contar < 5:
        lista.append(elemento)
        if lista:
            return lista
    else:
        return "El Largo de la Lista es mayor que 5"
# Fin
print(agregar_si(["perro", "gato", "delfin", "tortuga"], "caballo"))
print(agregar_si(["Francisco", "Rene", "Gonzalo", "Consuelo"], "Javier"))
print(agregar_si(["ruby", "javascript", "python", "c", "c#", "java"], "php"))


print("#######################################################")
"""
Crea una función llamada agregar_si que reciba una lista y un parámetro llamado nombre. 
La función debe agregar el nombre a la lista si el largo de la lista es menor a 5.
La función debe retornar la lista.
"""
# Escribe tu código aquí
def agregar_si(lista, nombre):
    if len(lista) < 5:
        lista.append(nombre)
        return lista
    else:
        return lista
# Fin
print(agregar_si(["perro", "gato", "delfin", "tortuga"], "caballo"))
print(agregar_si(["Francisco", "Rene", "Gonzalo", "Consuelo"], "Javier"))
print(agregar_si(["ruby", "javascript", "python", "c", "c#", "java"], "php"))

# Escribe tu código aquí
def limpiar_y_agregar(lista, nombre):
    nombre.strip()
    lista.strip()
    lista.append(nombre)
    return lista
# Fin
print(limpiar_y_agregar(["uno", "dos", "tres", "cuatro"], "       cinco"))
print(limpiar_y_agregar(["Camilo", "Ignacio", "Constanza"], "      Juana     "))
print(limpiar_y_agregar(["perro", "gato", "pájaro", "pez"], "    cabra   "))


print("#######################################################")
"""
Crea una función llamada limpiar_y_agregar que reciba una lista y un parámetro llamado nombre.
La función debe remover los espacios vacíos al inicio y al final del nombre y luego agregar el 
nombre al final de la lista. Finalmente, la función debe retornar la lista.
"""

# strip() | append() | 

# Escribe tu código aquí
def limpiar_y_agregar(lista, nombre):
    lista_clear = [item.strip() for item in lista]
    nombre_clear = nombre.strip()
    lista_clear.append(nombre_clear)
    return lista_clear
# Fin
print(limpiar_y_agregar(["uno", "dos", "tres", "cuatro"], "       cinco"))
print(limpiar_y_agregar(["Camilo", "Ignacio", "Constanza"], "      Juana     "))
print(limpiar_y_agregar(["perro", "gato", "pájaro", "pez"], "    cabra   "))


Crea una función llamada rotar_a_la_izquierda que reciba como parámetro una lista.
La función debe eliminar el primer elemento de la lista y luego agregar este mismo elemento al final. Retorna la lista modificada.

# Escribe tu código aquí
def rotar_a_la_izquierda(lista):
    my_lista = lista.pop(0) # Eliminamos el elemento deceado segun su indice de la lista 
    lista.append(my_lista) # Agregamos un elemento al final de la lista
    return lista
# Fin
print(rotar_a_la_izquierda(['uno','dos','tres','cuatro']))
print(rotar_a_la_izquierda([1,2,3,4]))
print(rotar_a_la_izquierda(['perro','gato','pájaro','pez']))

# Concatenacion de Lista 
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)  # [1, 2, 3, 4, 5, 6]


Crea una función llamada juntar_arreglos que reciba dos parámetros, arreglo1 y arreglo2, 
y retorne una nueva lista con los elementos de ambas listas excluyendo el primer elemento de cada una.

# Escribe tu código aquí
def juntar_arreglos(arreglo1, arreglo2):
    producto = arreglo1[1:] + arreglo2[1:]
    return producto
# Fin
print(juntar_arreglos([1,2,3,4], [5,6,7,8]))
print(juntar_arreglos(['a','b','c'], ['d','e','f']))
print(juntar_arreglos(['uno','dos','tres'], ['cuatro','cinco','seis']))

my_lista = list()
print(type(my_lista))
my_lista = [1 ,'Maria', 'Pepe', 'Marta', 'Antonio']
print(my_lista)
print(my_lista[-1])
print(type(my_lista))

print("######################################################")

my_Lista = [2 ,'Maria', 'Pepe', 'Marta', 'Antonio']
my_Lista.append("Zabdiel") # ---> Agregar elemento a una Lista (Alfinal de la lista).
my_Lista.insert(1,'John') # ---> Agregar elemento a una Lista en la posicion que desee (Utilizamos el indice)
my_Lista.extend(['Adriel', 'Clarybel', 'Loengri']) # --> Agregar varios elementos a una lista. 
my_Lista.remove("Marta") # --> Elimina un elemento de la lista
print(my_Lista)
print(my_Lista.index("Pepe")) # --> Validamos el Indice de un elemento en una lista
print("Loengri" in my_Lista) # --> Validar si un elemento existe en una lista (devuelve False o True)
print(my_Lista[2])
print(my_Lista[0:3]) 
print(my_Lista[:3])
print(type(my_Lista))
'''
def datosperson():
    datos = list()
    nom = input("Ingrese el Nombre: ")
    datos.append(nom)
    direc = input("Ingrese su Dirección: ")
    datos.append(direc)
    tel = input("Ingrese su numero de Telefono: ")
    datos.append(tel)
    print(datos)
datosperson()


# Lista 
def listas():
    hatList = [1, 2, 3, 4, 5]
    print(f"Lista Inicial: {' '.join(map(str, hatList))}")
    hatList[2] = int(input("Ingrese un Numero Entero: "))
    del hatList[-1]
    print(f"Lista Final: {' '.join(map(str, hatList))}")
    print(f"Total de Elementos en la Lista: {len(hatList)}")
listas()


'''
3.1.4.13 LAB: Los conceptos básicos de las listas - The Beatles
'''
def theBeatles():
    beatles = []
    print("Step 1:", beatles)
    
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")
    print(f"Step 2: {', '.join(map(str, beatles))}.")
    
    for member in range(2):
        beatles.append(input("New Band Member: "))
    print(f"Step 3: {', '.join(map(str, beatles))}.")
    
    del beatles[-1]
    del beatles[-1]
    print(f"Step 4: {', '.join(map(str, beatles))}.")
    
    beatles.insert(0, "Ringo Starr")
    print(f"Step 5: {', '.join(map(str, beatles))}.")
    
    print ("The Fab ", len(beatles))
theBeatles() 