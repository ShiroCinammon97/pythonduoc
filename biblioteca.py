'''
Programa: Sistema de bibliotecas.
Utilizar la lista de usuarios y personas definidas a continuación.
El programa debe mostrar un menú que permita:
1 - Buscar un usuario por su rut.
    1.1 - Si el usuario existe mostrar un menú para:
        1.1.1 - Realizar un préstamo de un libro
        1.1.2 - Realizar la devolución de un libro
            1.1.2.1 - Si el libro no existe, permitir registrar el libro que trajo la persona.
    1.2  - Si el usuario no existe, permitir registrar al usuario.
2 - Registrar un nuevo usuario.
3 - Registrar un nuevo libro.
4 - Salir
'''

usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": []},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]

def validar_rut(rut):
    for persona in usuarios:
        if rut == persona["rut"]:
            return True
    return False

def indice_por_rut(rut):
    for seleccionado, persona in enumerate(usuarios):
        if rut == persona["rut"]:
            return seleccionado
        
def registrar_nuevo_usuario(nombre, apellido, rut):
    usuarios.append({"nombre: ":nombre,"apellido": apellido, "rut": rut, "libros": []})
    print("Usuario ",nombre," ",apellido," registrado exitosamente")

def mostrar_libros():
    print("Seleccione que libro desea pedir prestado:")
    for item in libros:
        print("id", item["id"],", Título", item["titulo"],", Cantidad disponible", item["cantidad_disponible"])

def prestar_libro(id_seleccionada):
    print("Libro prestado: ", libros[id_seleccionada-1]["titulo"])
    print("Actualizando cantidad disponible...")
    libros[id_seleccionada-1]["cantidad_disponible"] -= 1
    usuarios[seleccionado]["libros"].append(libros[id_seleccionada-1]["titulo"])
    print("Cantidad disponible actual: ",libros[id_seleccionada-1]["cantidad_disponible"])
    print(usuarios[seleccionado])

def devolver_libro():
    libros.append(usuarios[seleccionado]["libros"])

'''def devolver_libro():
    usuarios[seleccionado]["libros"].append(libros["cantidad_dispobile"][0])
    usuarios[seleccionado]["libros"] =-1
    libros["cantidad_disponible"][0] =+ 1'''

def registrar_libro():
    pass

while True:
    opcion = int(input("Seleccione una opción\n1. Buscar un usuario por su rut\n2. Registrar un nuevo usuario\nRegistrar un nuevo libro\n4. Salir\n"))
    if opcion == 1:
        rut = input("Inserte rut")
        rut = rut.lower()
        if validar_rut(rut) == True:
            opcion_rut = int(input("Usuario validado, que quiere hacer?\n1. Pedir prestado un libro\n2. Devolver un libro\n"))
            if opcion_rut == 1:
                mostrar_libros()
                seleccionado = indice_por_rut(rut)
                id_seleccionada = int(input())
                prestar_libro(id_seleccionada)
            elif opcion_rut == 2:
                seleccionado = indice_por_rut(rut)
                devolver_libro()
            else:
                print("Inserte una opción válida")
        else:
            yes_no = int(input("Usuario no existe en directorio, quiere registrarlo?\n1. Sí\n2. No\n"))

            if yes_no == 1:
                nombre = input("Indique su nombre")
                apellido = input("Indique su apellido")
                registrar_nuevo_usuario(nombre, apellido, rut)
            elif yes_no == 2:
                pass
            else:
                print("Inserte una opción válida")
    elif opcion == 2:
            nombre = input("Indique su nombre")
            apellido = input("Indique su apellido")
            rut = input("Inserte rut")
            registrar_nuevo_usuario(nombre, apellido, rut)
    elif opcion == 3:
        devolver_libro()
    elif opcion == 4:
        print("Adios")
        break
    else:
        print("Inserte opción válida")

print("Test2")

