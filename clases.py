'''
Clases, objetos, métodos 
'''

# Crear Clase
class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

# Creando métodos 
def arrancar(self):
    self.enmarcha = True

def estado(self):
    if (self.enmarcha):
        return "El coche esta en Marcha"
    else:
        return "El coche esta parado"

# Crear un objeto o instancia 
micoche = Coche() # instanciar una clase

print(micoche.largoChasis)
print(micoche.ruedas)
micoche.arrancar()

print(micoche.estado())