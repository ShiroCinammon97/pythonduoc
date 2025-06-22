'''
Ejercicio: Sistema de votación secreta con detección de fraudes
Crea un sistema de votación en el que las personas pueden votar por un candidato. Cada votante debe identificarse con su ID de votante único. El sistema debe:

🧩 Requisitos:
Cada votante solo puede votar una vez.
No se deben aceptar IDs duplicados.
Cada voto se registra con el ID del votante y el candidato elegido.
El sistema termina cuando se ingresa "FIN" como ID de votante.
Al final, mostrar:
Cuántos votos recibió cada candidato.
Qué IDs intentaron votar más de una vez (fraude detectado).
'''
lista_id = []
id_fraude = []
fraudes = 0

def agregar_id(id_persona,opcion_voto):
    if len(lista_id) == 0:
        lista_id.append({"ID":id_persona,"Voto":opcion_voto})
        return True
    for persona in lista_id:
        if id_persona == persona["ID"]:
            print("ID duplicado. Intento de fraude")
            if id_persona not in id_fraude:
                id_fraude.append(id_persona)
            return False
        else:
            lista_id.append({"ID":id_persona,"Voto":opcion_voto})
            return True

def contador_votos(opcion_voto, lista_id):
    pass

while True:
    id_persona = input("Inserte su id\n")
    if id_persona == "FIN":
        print(lista_id)
        break
    try:
        opcion_voto = int(input("Inserte por el candidato que vota:\n1. Coca-cola man\n2. Pepsiman\n"))
    except ValueError as error:
        print("Error: ",error)
        print("Se esperaba un entero")
        opcion_voto = 0

    if opcion_voto == 1 or opcion_voto == 2:
        if agregar_id(id_persona,opcion_voto) == True:
            print("Gracias por su voto")
        else:
            fraudes += 1
    elif opcion_voto == 0:
        print("Ingrese un número entero")
    else:
        print("Ingrese una opción válida")
