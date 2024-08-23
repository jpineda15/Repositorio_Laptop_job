### Strings ###

my_strings = "Mi Strings"
my_other_strings = 'Mi otro String'

print (len(my_strings))
print (len(my_other_strings))

print (my_strings + ' ' + my_other_strings)

my_new_line_string = 'Este es un Strings\ncon salto de linea' # el caracter especial ( \n ) salto de Linea 
print (my_new_line_string)

my_tab_string = '\tEste es un Strings con tabulacion' # el caracter especial ( \t ) tabulacion 
print (my_tab_string)

# Formateo de texto

name, surname, age = "Juan", "Pineda", 35
print ("Mi Nombre es {} {} y mi edad es {}".format(name,surname,age))
print ("Mi Nombre es %s %s y mi edad es %d" %(name, surname, age))
print (f"Mi Nombre es {name} {surname} y mi edad es {age}") ### inferencia de datos 


### Desempaque de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# Division 

language_slice = language[1:3]
print(language_slice)

# Reverse

language_reversed = language[::-1]
print(language_reversed )

# Funciones 

print (language.capitalize())
print (language.upper())
print (language.count('t'))
print (language.isnumeric())
print ('2'.isnumeric())
print (language.lower())
print (language.startswith('py'))


## No, si yo escribo mi nombre completo, en vez de mostrar Franklyn Castro que muestre FC 
nom = str(input("Ingrese su Nombre: "))
ape = str(input("Ingrese su Apellido: "))
full_name = f"{nom[0]}{ape[0]}"
print("Iniciales: " + (full_name.upper()))



