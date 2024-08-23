### Exception Handling ###

n1 = 5
n2 = 1
n2 = '1'
#print(n1 + n2)
"""
if n1 > 3:
    print(n1 + n2)
else:
    print("No se cumplio")
"""
try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
