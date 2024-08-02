# Tarea Mod-3(ext-2)

colorList = [] 
colorList = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura']
colorList.append("Magenta")
print(f"Lista Completa: {colorList}")

new_color = ["Blanco", "Amarillo"] #-->nueva lista con valores a reemplazar. 
indeX = colorList.index('marrón') #--> Almacenamos el Indice del valor a reemplazar. 
colorList = colorList[:indeX] + new_color + colorList[indeX + 1:]
print(f"Lista Completa: {colorList}")

colorlist = colorList[5:8]
print(f"Los Colores quinto, sexto y séptimos: {colorlist}.")


colorlist = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura']
colorlist.remove("marrón") 
print(f"Eliminamos el Color 'marrón': {colorlist}.")

colorlist.pop(3)
print(f"Remueva el tercer elemento especificando el índice: {colorlist}.")

#colorlist = len(colorlist)
print(f"Imprima el número de elementos de la lista: {len(colorlist)}")





def colores():
    colorList = [] 
    colorList = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura']
    colorList.append("Magenta")
    print(colorList)
    
    new_color = ["Blanco", "Amarillo"] #-->nueva lista con valores a reemplazar. 
    indeX = colorList.index('marrón') #--> Almacenamos el Indice del valor a reemplazar. 
    colorList = colorList[:indeX] + new_color + colorList[indeX + 1:]
    print(f"Lista Completa: {colorList}")
    
    colorlist.remove("marrón") # --> El color marrón fue removido, estaremos colocando el que lo sustituyo
    #print(f"Eliminamos el Color 'marrón': {colorlist}.")
    #listColor = " ," .join(colorList)
    #print(f"Los Colores de Mi Lista: {listColor}.")
    #cololist = colorList[5:8]
    #colorlist = ", " .join(cololist) # Unir los elementos de colorList en una sola cadena, separados por comas y espacios.
    
    #colorList = list(colorlist)
    #colorList.remove("azul") # Eliminamos el segundo elemento de nuestra lista. 
    
colores()

