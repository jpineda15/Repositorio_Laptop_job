# Tarea Mod-3(ext-2)
"""
    Crear una lista vacía que se llame colorList y haga lo siguiente:
        -Insertar los siguientes colore (negro, azul, marrón, gris, verde, naranja, rosa, púrpura)
        -Agregar el color Magenta
        -Cambie el segundo valor, reemplazándolo con dos valores nuevos
        -Devuelva el quinto, sexto y séptimo elemento
        -Elimine el color marrón
        -remueva el tercer elemento especificando el índice
        -Imprima el número de elementos de la lista
"""


"""
    Algoritmo Informal para los pasos que dieron durante el proceso de la lista colorList
        1.  creamos la fusión colores(). 
        2.  Creamos la lista colorList[]. 
        3.  Insertamos una lista de elementos. 
        4.  Agregamos el elemento "Magenta" a la lista colorList[]. 
        5.  Imprimir colorList
        6.  Creamos nueva lista new_color[]
                Almacenamos el indice a reemplazar.
                Divide y combina la lista para reemplazar el valor en index con new_values.
                Imprimir nuevo resultado.
        7.  Imprimir las posiciones Quinto, Sexto y Séptimo. 
        8.  Eliminar el color marrón, que esta en el Index(2). 
                El color marrón fue sustituido en el proceso 6 , estaremos tomando el color que lo sustituyo.
        9.  Eliminar el elemento con indice 3
        10. Imprimir el Total de los elementos de la lista colorList[]
        11. Ejecutamos la fusión colores()
"""

def colores():
    colorList = [] 
    colorList = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura']
    colorList.append("Magenta") # usamos el método append() para agregar un elemento a lista. 
    print(colorList)
        
    new_color = ["Blanco", "Amarillo"] #-->nueva lista con valores a reemplazar. 
    indeX = colorList.index('marrón') #--> Almacenamos el Indice del valor a reemplazar. 
    colorList = colorList[:indeX] + new_color + colorList[indeX + 1:] # dividimos la cadena en dos los concatenamos | colorList[indeX + 1:] --> Esta parte contiene los elemento que están luego del que se va a reemplazar. 
    print(f"Lista Completa: {colorList}")
    
    print(f"Imprimir la Posición quinto, sexto y séptimo: {colorList[5:8]}")
    
    colorList.remove("Blanco") # --> El color marrón fue removido, estaremos colocando el color que lo sustituyo
    print(f"Eliminamos el Color 'marrón': {colorList}.")
    
    #colorList.pop(3)
    del colorList[3] # Eliminamos el color con el indice 3 de la lista
    print(f"Nuevo Valor lores: {colorList}")
    
    print(f"Total de Elementos de la Lista ColorList: {len(colorList)}")

colores()
