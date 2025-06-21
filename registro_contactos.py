'''
🧩 Ejercicio: Sistema de registro interactivo de contactos
Crea un programa que simule un sistema de gestión de contactos. El usuario puede:

Agregar un nuevo contacto
Ver todos los contactos
Buscar por nombre
Salir del programa

Cada contacto se guarda como un diccionario con las claves: "nombre", "teléfono" y "email". Todos los contactos se almacenan en una lista.

🧠 Requisitos técnicos:
Usa un bucle while True para mostrar el menú continuamente.
Si el usuario elige "4", el programa debe salir con break.

Usa funciones para mantener el código organizado:
agregar_contacto(lista)
ver_contactos(lista)
buscar_contacto(lista)
'''

lista = []

def agregar_contacto(lista):
    pass
def ver_contactos(lista):
    pass
def buscar_contacto(lista):
    pass
while True:
    try:
        opcion = int(input("Ingrese una opción:\n1. Agregar un nuevo contacto\n2. Ver todos los contactos\n3. Buscar por nombre\n4. Salir del programa\n"))
    except ValueError as error:
        print("Error: ",error)
        print("Se esperaba un número entero")
        opcion = 999
    if opcion == 1:
        agregar_contacto(lista)
    elif opcion == 2:
        ver_contactos(lista)
    elif opcion == 3:
        buscar_contacto(lista)
    elif opcion == 4:
        print("Adios")
        break
    elif opcion == 999:
        print("Inserte un número entero")
    else:
        print("Inserte una opción válida")