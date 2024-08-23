# Operadores Aritmeticos

print ('Suma (3 + 4) =', 3 + 4) # Suma
print ('Resta (3 - 4) =', 3 - 4) # Resta
print ('Multiplicación (3 * 4) =', 3 * 4) # Multiplicación
print ('División (3 / 4) =', 3 / 4) # División de punto flotante Ej: 2.333333
print ('Módulo (9 % 3) =', 9 % 3) # Módulo 
print ('División de piso (3 // 4) =', 3 // 4) # División entera o truncada Ej: 2
print ('Exponenciación (3 ** 4) =', 3 ** 4) # Exponenciación

print("###############################################")

# Operadores de comparación

print ('3 > 2 =', 3 > 2) # True, porque 3 es mayor que 2
print ('3 >= 2 =', 3 >= 2) # True, porque 3 es mayor que 2
print ('3 < 2 =', 3 < 2) # False, porque 2 es menor que 3
print ('2 < 3 =', 2 < 3) # True, porque 2 es menor que 3
print ('3 == 2 =', 3 == 2) # False, porque 3 no es igual 2
print ('3 != 2 =', 3 != 2) # True, porque 3 no es igual a 2
# con la funcion "len" podemos contar caracteres.
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

print("###############################################")

### Operadores de Logicos ###

print (3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (3 < 4 and "Hola" < "Python")
print (3 < 4 or "Hola" < "Python")
print (not(3 > 4))
