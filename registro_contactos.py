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

Si quieres seguir escalando, podrías implementar validación para evitar contactos duplicados (mismo nombre), o permitir borrar uno.
'''

lista = []

def agregar_contacto(lista):

    solo_numeros = False
    nombre = input("Inserte un nombre\n")
    while True:
        telefono = input("Inserte un número telefónico\n")
        for caracter in telefono:
            if caracter.isnumeric():
                solo_numeros = True
            else:
                solo_numeros = False
        if len(telefono) >= 9 and solo_numeros == True:
            for numero in lista:
                if telefono == contacto["telefono"]:
                    print("Número teléfonico ya registrado")
                else:
                    break
            break
        else:
            print("Inserte un numero telefónico válido")
    email = input("Inserte un email\n")
    
    contacto = {"nombre":nombre,"teléfono": telefono,"e-mail":email}
    lista.append(contacto)


def ver_contactos(lista):
    if len(lista) == 0:
        print("No hay contactos registrados, por favor agregue uno.")
    else:
        print(lista)

def buscar_contacto(lista):
    nombre_a_buscar = input("Inserte nombre de contacto que busca\n")
    if len(lista) == 0:
        print("No hay contactos registrados, por favor agregue uno.")
    else:
        for contacto in lista:
            if nombre_a_buscar == contacto["nombre"]:
                print(contacto)
            else:
                print("Contacto buscado no encontrado")

while True:
    try:
        opcion = int(input("Ingrese una opción:\n1. Agregar un nuevo contacto\n2. Ver todos los contactos\n3. Buscar por nombre\n4. Salir del programa\n"))
    except ValueError as error:
        print("Error: ",error)
        print("Se esperaba un número entero")
        opcion = 999
    if opcion == 1:
        agregar_contacto(lista)
        print(lista)
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