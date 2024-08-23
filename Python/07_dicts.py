### Ditionarios(Estructura de Datos) ##

'''my_dict = dict() # definimos un diccionarios.
my_other_dict = {} # definimos un diccionarios.

print(type(my_dict))
print(type(my_other_dict))

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }
print(my_dict)

my_other_dict = {
    "Nombre":"Juan",
    "Apellido":"Pineda",
    "Edad":"35",
    "Lenguaje": {"SQL", "Python", "Java"},
    1:1.30
    }
print(my_other_dict)
print(len(my_other_dict)) # Contamos la claves

print(my_dict["name"]) # Consultar la clave name

my_dict ["name"] = "Adriel" # Actualizando la clave name.
print(my_dict["name"])

my_other_dict["Calle"] = "Calle Jpineda" ## Agregar clave al dict
print(my_other_dict)

del my_other_dict["Calle"] # Eliminar una clave en nuestro dict
print(my_other_dict)

print("name" in my_dict)
print(my_dict)

## Dicionario
info = {
    "Name": input("Igrese su Nombre: "),
    "SurName": input("Igrese su Apellido: "),
    "Age": input("Ingrese su Edad: ")
}
print(info)
print(type(info))'''

# declarar Diccionario
mydiccionario = {
    "Alemania" : "Berlin",
    "Francia" : "Paris",
    "Repueblica Dominicana" : "Santo Domingo"
    }
print(mydiccionario)
print(mydiccionario["Francia"])
mydiccionario["Italia"] = "Liboa" # --> agregar contenido al diccionario
print(mydiccionario)
mydiccionario["Italia"] = "Roma" # --> Modificar diccionario
print(mydiccionario)
del mydiccionario["Italia"] # --> Eliminar un elemento del diccionario
print(mydiccionario)

myDiccionario = {
    23 : "Jordan",
    7 : "James",
    40 : "Curry",
    11 : "Durant",
    15 : "DeRozan",
    1 : "Irving",
    6 : "Lebron"
} 
print(myDiccionario)
print(myDiccionario.keys()) # --> Consultar las claves del diccionario
print(myDiccionario.values()) # --> Consultar los valores del diccionario
print(len(myDiccionario)) # --> Validar la logitud del diccionario