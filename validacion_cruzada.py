'''🧠 Ejercicio: Validación cruzada de inventario y ventas
Tienes dos listas:
Una lista de inventario, donde cada elemento es un diccionario con:

"producto": nombre del producto
"stock": cantidad disponible

Una lista de ventas registradas, donde cada elemento es un diccionario con:

"producto": nombre del producto vendido
"cantidad": unidades vendidas

Tu tarea es detectar si hay algún producto vendido que no existe en el inventario.

Escribe una función validar_ventas(inventario, ventas) que:
Recorra la lista de ventas usando índices.
Para cada venta, verifique si el producto vendido existe en el inventario.
Si encuentra un producto vendido no registrado, lo imprima con su índice.
Al final, diga si todo está bien o si hubo productos inválidos.

🧪 Ejemplo de salida esperada:

Producto no registrado en inventario: 'yogur' en índice 2 de ventas
Se encontraron errores en las ventas.
'''

inventario = [
    {"producto": "pan", "stock": 10},
    {"producto": "leche", "stock": 5},
    {"producto": "huevos", "stock": 30}
]

ventas = [
    {"producto": "leche", "cantidad": 2},
    {"producto": "pan", "cantidad": 1},
    {"producto": "yogur", "cantidad": 3}
]

def indexar_inventario(inventario):
    for indice_p, producto in enumerate(inventario):
            index_i = inventario[indice_p]["producto"]
            return index_i

def validar_ventas(inventario, ventas):
    index_inv = indexar_inventario(inventario)

    for indice_v, producto in enumerate(ventas):
        index_v = ventas[indice_v]["producto"]
        if index_inv != index_v:
             print("el producto: ", ventas[indice_v]["producto"])

validar_ventas(inventario, ventas)