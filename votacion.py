'''
Ejercicio: Análisis de votos de una encuesta
Un colegio realizó una encuesta para elegir el destino de una gira de estudios. 
Los resultados se almacenaron en una lista de diccionarios, 
donde cada diccionario representa un voto con la siguiente estructura:

Ejemplo:

votos = [
    {"estudiante": "Ana", "opcion": "Playa"},
    {"estudiante": "Luis", "opcion": "Montaña"},
    {"estudiante": "Sofía", "opcion": "Playa"},
    {"estudiante": "Pedro", "opcion": "Campo"},
    {"estudiante": "Ana", "opcion": "Montaña"},  # Voto repetido (no válido)
    ...
]


🧩 Tu desafío:
Crea una nueva lista que contenga sólo el primer voto válido de cada estudiante (ignorar votos repetidos).

Cuenta cuántos votos tiene cada opción usando un diccionario.

Muestra el índice en la lista original en que fue contado cada voto válido.

Determina y muestra la opción más votada.

🧪 Restricciones:
No uses tuplas, matrices (listas anidadas), ni números primos.

Debes usar listas, diccionarios, bucles for, y trabajar con índices.
'''
votos = []
total_votos = []

def agregar_votos(nombre_estudiante):
    voto_por_estudiante = {}
    voto_por_estudiante["estudiante"] = nombre_estudiante
    while True:
        try:
            opcion = int(input("Inserte opción para gira de estudios:\n1. Playa\n2. Montaña\n3. Campo\n"))
        except ValueError as error:
            print("Error: ",error)
            print("Se esperaba un valor entero")
            opcion = 0
        if opcion == 1:
            voto_por_estudiante["opción"] = "Playa"
            break
        elif opcion ==2:
            voto_por_estudiante["opción"] = "Montaña"
            break
        elif opcion == 3:
            voto_por_estudiante["opción"] = "Campo"
            break
        else:
            print("Elija una opción válida")
    votos.append(voto_por_estudiante)
    
    

def contar_votos(votos):
    
    contador_playa = 0
    contador_montana = 0
    contador_campo = 0

    for voto in votos.value[1]:
        cantidad_votos = {}
        if voto == "Playa":
            contador_playa += 1
        elif voto == "Montaña":
            contador_montana += 1
        else:
            contador_campo += 1
        cantidad_votos = {"Playa":contador_playa,"Montaña":contador_montana,"Campo":contador_campo}
    

    total_votos.append(cantidad_votos)
        


'''
def mostrar_votos():
    pass
'''


for estudiante in range(3):
    nombre_estudiante = input("Inserte nombre del estudiante")
    agregar_votos(nombre_estudiante)
    
contar_votos(votos)
    
print(votos)
print(total_votos)
