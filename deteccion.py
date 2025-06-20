'''
Ejercicio: Detección de valores repetidos por clave
Dada una lista de diccionarios, cada uno con las mismas claves, implementa una función que devuelva un nuevo diccionario que indique, 
para cada clave, los valores que se repiten entre al menos dos diccionarios.

🔢 Entrada de ejemplo:
python

datos = [
    {"nombre": "Ana", "edad": 30, "ciudad": "Lima"},
    {"nombre": "Luis", "edad": 25, "ciudad": "Lima"},
    {"nombre": "Carlos", "edad": 30, "ciudad": "Quito"},
    {"nombre": "Ana", "edad": 22, "ciudad": "Bogotá"}
]

'''

datos = [
    {"nombre": "Ana", "edad": 30, "ciudad": "Lima"},
    {"nombre": "Luis", "edad": 25, "ciudad": "Lima"},
    {"nombre": "Carlos", "edad": 30, "ciudad": "Quito"},
    {"nombre": "Ana", "edad": 22, "ciudad": "Bogotá"}
]

def detectar_repetidos(datos):
    datos_repetidos = {}
    nombres_repetidos = []
    nombres_unicos = []
    edad_unica = []
    edad_repetida = []
    ciudad_repetida = []
    ciudad_unica = []
    for clave in datos:
        if clave["nombre"] not in nombres_unicos:
            nombres_unicos.append(clave["nombre"])
        else:
            nombres_repetidos.append(clave["nombre"])

        if clave["edad"] not in edad_unica:
            edad_unica.append(clave["edad"])
        else:
            edad_repetida.append(clave["edad"])

        if clave["ciudad"] not in ciudad_unica:
            ciudad_unica.append(clave["ciudad"])
        else:
            ciudad_repetida.append(clave["ciudad"])
        
    datos_repetidos["nombre"] = nombres_repetidos
    datos_repetidos["edad"] = edad_repetida
    datos_repetidos["ciudad"] = ciudad_repetida

    print(datos_repetidos)

detectar_repetidos(datos)
            