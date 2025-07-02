'''
🛍️ Ejercicio: Sistema de Devoluciones en una Tienda Online
Una tienda online almacena los registros de ventas de productos en una lista de diccionarios. Cada venta tiene la siguiente estructura:
ventas = [
    {"cliente": "Ana", "producto": "zapatillas", "entregado": True, "devuelto": False},
    {"cliente": "Luis", "producto": "camisa", "entregado": True, "devuelto": True},
    {"cliente": "Sofía", "producto": "jeans", "entregado": False, "devuelto": False},
    {"cliente": "Ana", "producto": "gorro", "entregado": True, "devuelto": False},
    {"cliente": "Luis", "producto": "pantalones", "entregado": True, "devuelto": False},
]
Crea una función llamada clientes_con_posible_reclamo(ventas) que devuelva una lista con los nombres de los clientes que:
Tienen al menos un producto entregado que no devolvieron.
Y no tienen productos pendientes de entrega.
En resumen: son clientes que ya recibieron todo lo que pidieron y no devolvieron al menos una cosa, por lo tanto podrían hacer un reclamo más adelante.

✅ Resultado esperado para el ejemplo anterior:
_____________________________________________________________
["Ana", "Luis"]
Ana: recibió zapatillas y gorro, no devolvió ninguno, no tiene entregas pendientes.
_____________________________________________________________

Luis: recibió camisa (la devolvió) y pantalones (no lo devolvió). No tiene entregas pendientes.

Sofía: tiene una entrega pendiente, queda fuera.
'''

ventas = [
    {"cliente": "Ana", "producto": "zapatillas", "entregado": True, "devuelto": False},
    {"cliente": "Luis", "producto": "camisa", "entregado": True, "devuelto": True},
    {"cliente": "Sofía", "producto": "jeans", "entregado": False, "devuelto": False},
    {"cliente": "Ana", "producto": "gorro", "entregado": True, "devuelto": False},
    {"cliente": "Luis", "producto": "pantalones", "entregado": True, "devuelto": False},
]

def clientes_reclamo():
    clientes = []
    for venta in ventas:
        for clave in venta:
            if venta["entregado"] == True and venta["devuelto"] == False:
                if venta["cliente"] not in clientes:
                    clientes.append(venta["cliente"])
    print(clientes)

clientes_reclamo()