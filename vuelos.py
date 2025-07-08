'''
Ejercicio preparación examen
transversal 2025-1
Enunciado:
El aeropuerto de santiago necesita un sistema con el cual poder gestionar los vuelos entre ciudades. La
información de los vuelos está registrada en un diccionario llamado “vuelos_chile”, donde las keys
(claves) corresponden al código único de cada vuelo compuesto por las dos primeras letras de la ciudad
de origen y las dos primeras letras de la ciudad de destino. El valor de cada clave contiene una lista con
los siguientes elementos: ciudad de origen, ciudad de destino, fecha del vuelo, hora del vuelo, puerta de
acceso al avión.
Por otra parte, se registra un diccionario llamado “info_vuelos”, donde las keys (claves) corresponden a
los mismos códigos únicos de cada vuelo y el valor es una lista con los siguientes elementos: valor del
pasaje, cantidad de asientos disponibles y el detalle de los asientos disponibles. Los puntos suspensivos
indican que pueden existir más elementos en los diccionarios.

Se muestra una imagen con el tipo de asientos que tienen los aviones:

El aeropuerto necesita:
1. Poder buscar vuelos según filtros de precio, lugar de origen, lugar destino y combinación de
lugar de origen y destino.
2. Realizar una compra donde se registren las personas a viajar con su nombre, rut y un asiento
aleatorio ya que en esta empresa se realizan vuelos económicos y no es posible elegir el vuelo.
3. Mostrar el stock de pasajes de los vuelos, mostrando todos o filtrando según ciudad de origen,
destino y ciudad destino.
El programa debe manejar cualquier tipo de excepción de errores posible y comportarse de una manera
amigable con el usuario, entregando mensajes que entreguen información fácil de entender y que
describa los procesos que el sistema está realizando, así también, como entregar resultados de una
manera intuitiva de entender.
'''

pasajes_comprados = {}

vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 1"],
    "ARCO": ["Arica", "Concepción", "2025-07-11", "14:45", "Puerta 2"],
    "COTO": ["Copiapo", "Tocopilla", "2025-07-12", "10:20", "Puerta 3"],
    "ANTI": ["Antofagasta", "Iquique", "2025-07-13", "07:15", "Puerta 4"],
    "VAOS": ["Valdivia", "Osorno", "2025-07-14", "09:50", "Puerta 5"],
    "SELA": ["Serena", "La Serena", "2025-07-15", "13:00", "Puerta 6"],
    "RIAN": ["Rancagua", "Antofagasta", "2025-07-16", "17:25", "Puerta 7"],
    "TEAR": ["Temuco", "Arica", "2025-07-17", "12:10", "Puerta 8"],
    "CHIQ": ["Chillán", "Quellón", "2025-07-18", "11:30", "Puerta 9"],
    "PACO": ["Puerto Aysén", "Coyhaique", "2025-07-19", "15:40", "Puerta 10"],
    "PUAN": ["Puerto Aysén", "Antofagasta", "2025-07-30", "09:15", "Puerta 11"],
    "SEPU": ["Serena", "Puerto Aysén", "2025-07-31", "07:30", "Puerta 12"],
    "VIAR": ["Viña del Mar", "Arica", "2025-08-01", "10:45", "Puerta 13"],
    "COTE": ["Copiapo", "Temuco", "2025-08-02", "06:50", "Puerta 14"],
    "AROS": ["Arica", "Osorno", "2025-08-03", "14:10", "Puerta 15"],
    "PUVI": ["Puerto Aysén", "Villarrica", "2025-08-04", "16:20", "Puerta 1"],
    "RITE": ["Rancagua", "Temuco", "2025-08-05", "11:35", "Puerta 2"],
    "CHCO": ["Chillán", "Coquimbo", "2025-08-06", "12:45", "Puerta 3"],
    "COAR": ["Coquimbo", "Arica", "2025-08-07", "13:55", "Puerta 4"],
    "TEPU": ["Temuco", "Puerto Aysén", "2025-08-08", "15:10", "Puerta 5"],
    "VAQU": ["Valdivia", "Quellón", "2025-08-09", "17:00", "Puerta 6"],
    "QUSE": ["Quellón", "Serena", "2025-08-10", "08:10", "Puerta 7"],
    "SERO": ["Serena", "Rancagua", "2025-08-11", "09:45", "Puerta 8"],
    "VIAN": ["Viña del Mar", "Antofagasta", "2025-08-12", "11:20", "Puerta 9"],
    "SERI": ["Santiago", "Rancagua", "2025-08-13", "06:30", "Puerta 10"],
    "IQPU": ["Iquique", "Puerto Aysén", "2025-08-14", "13:25", "Puerta 11"],
    "ANOS": ["Antofagasta", "Osorno", "2025-08-15", "10:00", "Puerta 12"],
    "QUCO": ["Quellón", "Concepción", "2025-08-16", "16:40", "Puerta 13"],
    "VALA": ["Valparaíso", "La Serena", "2025-08-17", "12:00", "Puerta 14"],
    "PUVA": ["Puerto Aysén", "Valparaíso", "2025-08-18", "14:20", "Puerta 15"]
}

info_vuelos = {
    "SAPA": [75000, 45, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C']],
    "ARCO": [68000, 30, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F']],
    "COTO": [72000, 20, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E']],
    "ANTI": [59000, 50, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C', '8D', '8E', '8F', '8J', '8K']],
    "VAOS": [65000, 25, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A']],
    "SELA": [40000, 60, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C', '8D', '8E', '8F', '8J', '8K', '8L', '9A', '9B', '9C', '9D', '9E', '9F', '9J', '9K', '9L']],
    "RIAN": [88000, 15, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L']],
    "TEAR": [91000, 35, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B']],
    "CHIQ": [56000, 40, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J']],
    "PACO": [97000, 10, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D']],
    "PUAN": [89000, 22, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J']],
    "SEPU": [67000, 27, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C']],
    "VIAR": [84000, 18, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C']],
    "COTE": [71000, 33, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L']],
    "AROS": [76000, 19, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D']],
    "PUVI": [88000, 24, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L']],
    "RITE": [73000, 28, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D']],
    "CHCO": [61000, 31, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J']],
    "COAR": [86000, 16, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A']],
    "TEPU": [93000, 13, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J']],
    "VAQU": [78000, 21, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F']],
    "QUSE": [65000, 36, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C']],
    "SERO": [69000, 29, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E']],
    "VIAN": [92000, 12, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F']],
    "SERI": [54000, 48, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E', '7F', '7J', '7K', '7L', '8A', '8B', '8C', '8D', '8E', '8F']],
    "IQPU": [96000, 11, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E']],
    "ANOS": [88000, 26, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B']],
    "QUCO": [67000, 23, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K']],
    "VALA": [60000, 38, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K', '4L', '5A', '5B', '5C', '5D', '5E', '5F', '5J', '5K', '5L', '6A', '6B', '6C', '6D', '6E', '6F', '6J', '6K', '6L', '7A', '7B', '7C', '7D', '7E']],
    "PUVA": [94000, 14, ['3A', '3B', '3C', '3J', '3K', '3L', '4A', '4B', '4C', '4D', '4E', '4F', '4J', '4K']],
}

def mostrar_todos_vuelos(vuelos_chile):
    for vuelo in vuelos_chile:
        print(vuelo, ": ",vuelos_chile[vuelo])

def filtrar_origen(vuelos_chile):
    origen = input("Ingrese el origen\n")
    encontrado = False

    for vuelo in vuelos_chile:
        if origen == vuelos_chile[vuelo][0]:
            print(vuelo, ": ",vuelos_chile[vuelo])
            encontrado = True

    if encontrado == False:
        print("No se encontraron vuelos\n")
        return False

def buscar_destino(vuelos_chile,info_vuelos):
    pass

def buscar_precio(vuelos_chile,info_vuelos):
    pass

while True:
    try:
        opcion = int(input("Seleccione una opción:\n1. Ver vuelos disponibles.\n2. Ver asientos disponibles.\n3. Comprar pasaje.\n4. Ver pasajes comprados.\n5. Salir.\n"))
    except ValueError as error:
        print("Error: ",error)
        print("Se esperaba un entero")
    if opcion == 1:
        #mostrar_todos_vuelos(vuelos_chile)
        filtrar_origen(vuelos_chile)
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        print("Adios")
        break
    else:
        print("Ingrese una opción válida")




'''                print("Seleccione una opción de filtro:")
            print("1. Ver todos los vuelos")
            print("2. Ver vuelos por origen")
            print("3. Ver vuelos por destino")
            print("4. Ver vuelos por origen - destino")
            print("5. Volver al menú principal")'''