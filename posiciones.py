'''
Ejercicio: Buscador de posiciones de un producto
Tienes una lista de pedidos, cada uno representado por un diccionario.
Cada pedido tiene el nombre del cliente y el producto que pidió.

Tu tarea es permitir que el usuario escriba el nombre de un producto, 
y tu programa debe devolver todas las posiciones (índices) en las que ese producto aparece en la lista de pedidos.

Crea una función buscar_indices_producto(pedidos) que:
1- Pida al usuario que ingrese un nombre de producto (por input()).
2- Recorra la lista usando índices.
3- Devuelva una lista de índices donde el producto coincida con lo ingresado.
4- Si no se encuentra, devuelve una lista vacía y un mensaje

'''


pedidos = [
    {"cliente": "Ana", "producto": "laptop"},
    {"cliente": "Luis", "producto": "monitor"},
    {"cliente": "Sofía", "producto": "teclado"},
    {"cliente": "Pedro", "producto": "monitor"},
    {"cliente": "Lucía", "producto": "laptop"},
    {"cliente": "María", "producto": "teclado"}
]

def indexar_producto(pedidos):
    encontrado = False
    producto = input("Ingrese el nombre del producto\n")

    for indice, pedido in enumerate(pedidos):
        for clave in pedido:
            if pedido["producto"] == producto:
                print("El indice del producto es:", indice)
                encontrado = True
    if encontrado == True:
        return True
    else:
        return False
while True:
    if indexar_producto(pedidos):
        break
    else:
        print("Producto no encontrado")
