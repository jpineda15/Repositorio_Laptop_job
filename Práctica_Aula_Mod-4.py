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
        print("Bienvenido a Compras en Linea JFP.")
        print()
        producto = input("¿Ingrese el Nombre del Producto que desea? ").upper().strip()
        print()
        cantidad = int(input(f"Por favor, Ingrese la Cantidad de '{producto}' que usted necesita? ")) 
        if cantidad > 10: 
                print("Su pedido se enviará mañana. La cantidad de artículos es mayor a 10.")
        print()
        pago = input("De sea Realizar el Pago (Si o No): ").upper().strip()
        if pago == 'SI':
                print()
                envió = input("La compra es con envío a domicilio. (Si o No): ").upper().strip()
                if envió == 'SI' and cantidad <= 10:
                        print()
                        print("El pedido ha sido pagado y enviado.")
                elif pago == 'SI' and cantidad > 10:
                        print()
                        print("El pago ha sido realizado, pero el producto aún no ha sido enviado.")
                else:
                        print()
                        print("El Pedido se Retirado en el Local.")
        else:
                print()
                print("El pedido no ha sido pagado. Realice el pago para procesar el envío.")
        print()
        print("Gracias por Preferirnos.")
pedidos()