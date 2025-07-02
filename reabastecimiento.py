'''
 Ejercicio: Inventario de Reabastecimiento Automático
Tienes un sistema de inventario de una tienda que contiene información sobre productos. Cada producto tiene:

Un nombre
Un stock actual
Un mínimo requerido para operar
Una lista con los últimos días en que se vendió
Tienes la siguiente estructura de datos inicial (esto puedes cambiarlo si haces tus propias pruebas):

inventario = [
    {"nombre": "manzanas", "stock": 4, "minimo": 5, "ventas_recientes": ["lunes", "miércoles", "viernes"]},
    {"nombre": "pan", "stock": 2, "minimo": 3, "ventas_recientes": ["martes"]},
    {"nombre": "leche", "stock": 10, "minimo": 4, "ventas_recientes": []},
    {"nombre": "huevos", "stock": 1, "minimo": 6, "ventas_recientes": ["lunes", "martes", "miércoles", "jueves", "viernes"]}
]

funcion que:
1- Recorra la lista de productos.
2- Agregue a una nueva lista aquellos productos cuyo stock sea menor al minimo.
3- En esa nueva lista, cada producto debe representarse con un diccionario que contenga:
nombre
4- cantidad_a_reabastecer (diferencia entre minimo y stock)

prioridad:

"alta" si el producto se vendió más de 3 días distintos.
"media" si se vendió al menos 1 día.
"baja" si no tiene ventas recientes.

La función debe devolver esta lista final de productos a reabastecer.
'''


inventario = [
    {"nombre": "manzanas", "stock": 4, "minimo": 5, "ventas_recientes": ["lunes", "miércoles", "viernes"]},
    {"nombre": "pan", "stock": 2, "minimo": 3, "ventas_recientes": ["martes"]},
    {"nombre": "leche", "stock": 10, "minimo": 4, "ventas_recientes": []},
    {"nombre": "huevos", "stock": 1, "minimo": 6, "ventas_recientes": ["lunes", "martes", "miércoles", "jueves", "viernes"]}
]

por_reabastecer = []

def reabastecer(inventario):
    for item in inventario:
        if item["stock"] < item["minimo"]:
            diferencia = int(item["minimo"])-int(item["stock"])

            if len(item["ventas_recientes"]) > 3: 
                prioridad = "alta"
            elif len(item["ventas_recientes"]) >= 1:
                prioridad = "media"
            elif len(item["ventas_recientes"]) == 0:
                prioridad = "baja"

            por_reabastecer.append({"Nombre":item["nombre"],"Cantidad a reabastecer":diferencia,"Prioridad":prioridad})

    print(por_reabastecer)
    
print("Productos por reabastecer:")
reabastecer(inventario)