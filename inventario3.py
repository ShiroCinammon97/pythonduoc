'''🔹 Ejercicio 1: Gestión de inventario por lotes
Enunciado:
Tienes una lista de productos vendidos y un diccionario que representa el inventario con su cantidad.
Actualiza el inventario restando la cantidad vendida de cada producto.
Si algún producto no existe en el inventario, ignóralo.
Si la cantidad llega a 0, elimínalo del inventario.

Objetivo esperado:
El diccionario inventario debe reflejar las cantidades restantes después de aplicar las ventas.
No debe contener productos con cantidad 0.
'''


ventas = ["lápiz", "cuaderno", "lápiz", "borrador", "lápiz", "cuaderno"]

inventario = {
    "lápiz": 3,
    "cuaderno": 2,
    "borrador": 1,
    "regla": 5
}

def resta_inventario(ventas,inventario):
    for item_v in ventas:
        for item_i in inventario:
            if item_v in item_i:
                item_i -= 1
    print(inventario)


    #for item in ventas:

resta_inventario(ventas,inventario)