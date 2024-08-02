# Tarea Mod-3(ext-2)

def colores():
    colorList = []
    colorList = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura']
    colorList.append("Magenta") # Usamos el Método append() para agregar el color Magenta a la colorList. 
    new_color = ["Blanco", "Amarillo"] #-->nueva lista con valores a reemplazar. 
    indeX = colorList.index('marrón') #--> Almacenamos el Indice del valor a reemplazar. 
    colorList = colorList[:indeX] + new_color + colorList[indeX + 1:]
    listColor = " ," .join(colorList)
    print(f"Los Colores de Mi Lista: {listColor}.")
    cololist = colorList[5:8]
    colorlist = ", " .join(cololist) # Unir los elementos de colorList en una sola cadena, separados por comas y espacios.
    print(f"Los Colores quinto, sexto y séptimos: {colorlist}.")
    colorList = list(colorlist)
    #colorList.remove("azul") # Eliminamos el segundo elemento de nuestra lista. 
    print(f"Eliminamos el Color 'marrón': {colorList}.")
colores()

