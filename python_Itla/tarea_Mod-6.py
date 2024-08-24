"""
Instrucciones:

1) Crear un Archivo de Texto Inicial:

Crea un archivo de texto llamado datos.txt que contenga una sola frase, como por ejemplo:
    -JavaScript es fácil de aprender
2) Leer el Archivo:

Abre el archivo datos.txt en modo lectura.
Lee el contenido del archivo y almacénalo en una variable.
3) Manipular la Cadena de Texto:

Convierte toda la cadena a mayúsculas.
Reemplaza la palabra "JavaScript" por "Python".
4) Escribir el Resultado en un Nuevo Archivo:

Crea un nuevo archivo llamado resultado.txt.
Escribe la cadena modificada en el nuevo archivo.
"""

with open('c:/Users/jpineda/Desktop/PythonGit/python_Itla/datos.txt', 'r', encoding = 'utf-8') as archivo:
    # pasamos la frase que contiene el archivo datas.txt a la variable texto
    texto = archivo.read().split('\n') # read(r) leer | split('\n') eliminamos el salto de linea del \n
    print(texto)
    # Trasformamos el contenido de la lista a texto normal y Convertimos en Mayúscula
    normal_text = ''.join(texto).upper() 
    # Imprimimos el proceso hasta este punto
    print(normal_text)
    # Reemplazamos la frase "TRANSACT-SQL" por "Python" utilizando la fusion replace()
    normal_text = normal_text.replace("TRANSACT-SQL", "Python").upper() 
    # Imprimimos el proceso hasta este punto 
    print(normal_text)
# Creamos un nuevo archivo "resultado.txt"
with open('c:/Users/jpineda/Desktop/PythonGit/python_Itla/resultado.txt', 'w', encoding = 'utf-8') as new_archivo:
    new_archivo.write(normal_text) # Pasamos el contenido de la variable normal_text