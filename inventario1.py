inventario = {}
totales = {}

def agregar_producto(inventario, nombre_producto):
    cantidad_por_producto = []
    for producto in range(3):
        while True:
            try:
                cantidades = int(input("Ingrese cantidad de producto específico en el depósito "))
            except ValueError as error:
                print("Error: ",error)
                print("Se esperaba una variable entera")
                cantidades = -1
            if cantidades < 0:
                print("Inserte una cantidad válida")
            else:
                cantidad_por_producto.append(cantidades)
                break
    inventario[nombre_producto] = cantidad_por_producto

def stock_total(inventario):
    for producto in inventario:
        total = sum(inventario[producto])
        totales[producto] = total
    return totales
    

for item in range(3):
    nombre_producto = input("Ingrese el nombre de su producto")
    agregar_producto(inventario,nombre_producto)

stock_total(inventario)

print(inventario)
print(totales)