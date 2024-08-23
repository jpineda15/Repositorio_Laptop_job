'''
3.1.2.15 LAB: Hipótesis de Collatz
'''
def hipótesis():
    c0 = int(input("Ingrese c0: "))
    if c0 > 1:
        pasos = 0
        while c0 != 1:
            if c0 % 2 != 0:
                cnuevo = 3 * c0 + 1
            else:
                cnuevo = c0 // 2
            print(c0)
            c0 = cnuevo
            pasos += 1
        print("El número de pasos fue: ", pasos)
    else:
        print("El número debe ser mayor a 1")
hipótesis()

