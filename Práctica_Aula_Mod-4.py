'''
Realizar un programa que solicite al usuario información sobre un pedido,
incluyendo el nombre del producto, la cantidad solicitad, el estado del pago (si o no), y el estado del envió (si o no).
El programa debe utilizar decisiones anidadas para verificar el estado del pedido e imprimir un mensaje correspondiente según las siguientes 
Condiciones:
        Si el pago ha sido realizado y el producto ha sido enviado, imprimir: 'El pedido ha sido pagado y enviado.'
        Si el pago ha sido realizado pero el producto aun no ha sido enviado, imprimir: 'El pago ha  sido realizado, pero el producto aun no ha sido enviado.'
        Si el pago no ha sido realizado, imprimir: 'El pedido no ha sido pagado. Realice el pago para procesar el envió.
Asegúrate de manejar tanto las repuestas afirmativas como las negativas del usuario de manera adecuada. Utiliza decisiones anidadas para 
estructurar tu programa de manera clara. 
'''

def pedidos():
        print()
        print("Bienvenido. Por favor, ingrese su solicitud.")
        print()
        producto = input("¿Qué producto deseas pedir? ").upper()
        print()
        cantidad = int(input(f"¿Cuántos '{producto}' deseas pedir? ")) 
pedidos()