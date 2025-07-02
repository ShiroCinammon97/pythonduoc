'''
Ejercicio: Sistema de corrección de errores en pedidos
Tienes una lista de pedidos realizados por clientes. Cada pedido es un diccionario con los siguientes datos:

pedidos = [
    {"cliente": "Ana", "producto": "laptop", "cantidad": 1},
    {"cliente": "Luis", "producto": "monitor", "cantidad": 2},
    {"cliente": "Sofía", "producto": "teclado", "cantidad": 3},
    {"cliente": "Luis", "producto": "mouse", "cantidad": 1}
]

🎯 Tu tarea
1. Crea una función llamada corregir_pedido(pedidos) que:
-Pregunte al usuario el índice del pedido a corregir.
-Si el índice es válido, muestre el contenido del pedido original.
-Pregunte al usuario qué campo desea modificar (cliente, producto o cantidad).
-Pida el nuevo valor y lo reemplace en el diccionario correspondiente.
-Muestre el pedido actualizado.
2. Si el índice está fuera de rango, mostrar un mensaje de error y volver a pedir el índice (usando un while).
3. El programa debe terminar después de una sola corrección exitosa.
'''


pedidos = [
    {"cliente": "Ana", "producto": "laptop", "cantidad": 1},
    {"cliente": "Luis", "producto": "monitor", "cantidad": 2},
    {"cliente": "Sofía", "producto": "teclado", "cantidad": 3},
    {"cliente": "Luis", "producto": "mouse", "cantidad": 1}
]

def buscar_producto(pedidos,pedido):
    for item in pedidos:
        if pedido == item["producto"]:
            return True
        else:
            print("Pedido no encontrado")
            return False

def corregir(pedidos):
    pedido = input("Que pedido desea corregir?\n")
    if buscar_producto(pedidos,pedido):
        print("ok")
    try:
        campo = int(input("Qué campo desea modificar?\n1. cliente\n2. producto\n3. cantidad\n"))
    except ValueError as error:
        print("Error: ",error)
        print("Se esperaba un número entero")
        campo = 0

    nuevo_valor = input("Ingrese el nuevo valor que reemplazará al anterior\n")
    
    if campo == 1:
        pedidos["cliente"] = nuevo_valor
    elif campo == 2:
        pedidos["producto"] = nuevo_valor
    elif campo == 3:
        pedidos["cantidad"] = int(nuevo_valor)
    elif campo == 0:
        print("Inserte un número entero")
    else:
        print("Inserte un número válido")
    
    print(pedidos)

corregir(pedidos)
