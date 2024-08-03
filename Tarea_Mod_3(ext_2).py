# Tarea Mod-3(ext-2)

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
    colorList.append("Magenta")
    print(colorList)
    
    new_color = ["Blanco", "Amarillo"] #-->nueva lista con valores a reemplazar. 
    indeX = colorList.index('marrón') #--> Almacenamos el Indice del valor a reemplazar. 
    colorList = colorList[:indeX] + new_color + colorList[indeX + 1:]
    print(f"Lista Completa: {colorList}")
    
    print(f"Imprimir la Posición quinto, sexto y séptimo: {colorList[5:8]}")
    
    colorList.remove("Blanco") # --> El color marrón fue removido, estaremos colocando el color que lo sustituyo
    print(f"Eliminamos el Color 'marrón': {colorList}.")
    
    colorList.pop(3)
    print(f"Nuevo Valor lores: {colorList}")
    
    print(f"Total de Elementos de la Lista ColorList: {len(colorList)}")

colores()

