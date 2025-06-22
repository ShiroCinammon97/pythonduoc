'''
Ejercicio: Detectar registros duplicados según múltiples campos
Crea un programa que permita ingresar múltiples personas (una por línea), con su nombre y correo electrónico. Cada entrada debe almacenarse como un diccionario en una lista.

El programa debe detectar si ya existe una persona con el mismo nombre o con el mismo correo, e impedir su registro duplicado.

Requisitos:
Usar solo listas y diccionarios.

Detectar duplicados por nombre o por correo.

Mostrar un mensaje si se detecta duplicado.

El programa termina cuando se ingresa "FIN" como nombre.
'''
 
def validar_correo(correo):
    if "@gmail.com" not in correo and "@outlook.com" not in correo:
        print("Ingrese un correo válido")
        return False
    else:
        print(correo)
        return True



nombre = input("Ingrese el nombre")
while True:
    correo = input("Ingrese el correo")
    if validar_correo(correo) == True:
        break