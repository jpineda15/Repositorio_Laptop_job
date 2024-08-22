'''
1 readlines() --> nos permite imprimir la primera Linea.

r --> read(lectura)
t --> text-mode
w --> write(escritura)
a --> append(Agregar contenido)
x --> create 
b --> bytes - para archivos como fotos
encoding = 'utf-8' --> esta parte es optional(codificación de caracteres)
'''
"""
File = open('C:/Users/jpineda/Desktop/PythonGit/fichero.txt', 'r', encoding = 'utf-8')
#primerLinea = file.readline()
print(File)
linea = File.readlines()
print(linea)
File.close() #Cerramos el documento
"""


"""
# with nos permite cerrar el archivo automáticamente termine de usarlo.
with open('C:/Users/jpineda/Desktop/PythonGit/data.txt', 'r') as archivo:
    oneLine = archivo.readline()
    linea = archivo.readlines()
    print(linea)
    print("Nos muestra una Linea del archivo: ", oneLine)

# iteramos en el archivo usando el bucle for
for i in linea:
    print(i.replace('\n', '')) #replace() nos permite modificar el contenido 
"""

with open('C:/Users/jpineda/Desktop/PythonGit/data.txt', 'r') as archivo:
    print(archivo.read().split('\n')) # read(r) leer | split('\n') eliminamos el salto de linea del \n

with open('./data.txt', 'r') as archivo:
    print(archivo.read().split('\n')) 

#fichero = open('./datas.txt', 'rt', encoding='utf-8')
