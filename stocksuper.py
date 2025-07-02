'''
Un supermercado lleva el control de su inventario con una lista de diccionarios. 
Cada diccionario representa un producto:
Crea una función llamada buscar_reposicionables que devuelva una lista con los índices de los productos que están sin stock (stock == 0) 
y que pertenecen a una categoría donde otro producto sí tiene stock.

✅ Resultado esperado con el ejemplo anterior:
___________________________________________________________________________________________
[0, 2]
___________________________________________________________________________________________
Índice 0: "pan" → sin stock, otro alimento (leche) sí tiene stock.
Índice 2: "jabón" → sin stock, otro de higiene (detergente) sí tiene stock.
Índice 4: "queso" → también sin stock, pero ya se contó la categoría "alimentos" antes (no se repite).
'''

productos = [
    {"nombre": "pan", "stock": 0, "categoria": "alimentos"},
    {"nombre": "leche", "stock": 5, "categoria": "alimentos"},
    {"nombre": "jabón", "stock": 0, "categoria": "higiene"},
    {"nombre": "detergente", "stock": 2, "categoria": "higiene"},
    {"nombre": "queso", "stock": 0, "categoria": "alimentos"}
]

def buscar_repo():
    repo = []
    for indice_prod, producto in enumerate(productos):
        if producto["stock"] <= 0:
            repo.append([indice_prod])
    print(repo)


buscar_repo()