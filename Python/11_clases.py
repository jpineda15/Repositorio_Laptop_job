### classes ###
print("#######################################################################")
class Person:  # declarando una clase
    pass 

print(Person) # Podemos impreir la clase sin parentesis.
print(Person()) # Clases con parentesis.

print("#######################################################################")

class Myperson:
    def __init__(self, name, surname): # Metodo especial que se llama cuando se crea 
        self.name = name
        self.surname = surname

my_person = Myperson("John", "Pineda")
print(my_person)
print(my_person.name)
print(my_person.surname)
print(f"{my_person.name} {my_person.surname}")

print("#######################################################################")


class Myotherperson:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
    
    def walk(self):
        print(f"{self.full_name} esta caminando")

person2 = Myotherperson("Adriel", "Pineda")
print(person2)
person2.walk()
