'''
Ejercicio: Inventario de productos y cálculo de stock total
Crea un programa que administre un pequeño inventario de productos, registrando su cantidad en diferentes depósitos. 
Luego, debe calcular cuántas unidades hay en total por producto.

🧾 Requisitos:
Crea una función agregar_producto(inventario, nombre_producto, cantidades) que:
Reciba un diccionario inventario, un nombre_producto (string) y una lista cantidades (enteros) que representan las unidades disponibles en varios depósitos.
Agregue esta información al inventario (el producto como clave y las cantidades como valor).
Crea una función stock_total(inventario) que:
Reciba el diccionario inventario.
Devuelva un nuevo diccionario donde cada clave sea el nombre del producto y el valor sea la suma total de unidades disponibles en todos los depósitos.
Crea una función mostrar_stock(stock_dict) que:
Imprima: "Producto: <nombre>, Stock total: <cantidad>" para cada producto.
Registra al menos 3 productos, con 3 cantidades cada uno (como si estuvieran en 3 depósitos distintos).
'''
inventario = {}
totales = {}

def agregar_producto(inventario, nombre_producto):
    cantidad_por_producto = []
    for producto in range(3):
        cantidades = int(input("Ingrese cantidad de producto específico en el depósito "))
        cantidad_por_producto.append(cantidades)
    inventario[nombre_producto] = cantidad_por_producto

def stock_total(inventario):
    pass

def mostrar_stock(stock_dict):
    pass

for item in range(3):
    nombre_producto = input("Ingrese el nombre de su producto")
    agregar_producto(inventario,nombre_producto)

print(inventario)