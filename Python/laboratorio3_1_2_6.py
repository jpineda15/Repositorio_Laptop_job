'''
    3.1.2.6 LAB: Conceptos básicos del bucle for - contando Mississippi 
'''

def contando():
    import time
    for second in range(1,6):
        print(f"{second} Mississippi.")
        time.sleep(1)
    print("Ready or not here I come.")
contando()  # Llama a la función contando() para ejecutar el bucle for