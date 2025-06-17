estudiantes = {}
promedios_local = {}

def agregar_estudiantes(estudiantes,nombre):
    lista_notas = []
    for nota in range(n_notas):
        try:
            nota = float(input("Inserte su nota"))
        except ValueError as error:
            print("Error: ", error)
            print("El valor debió haber sido un reak")
            nota = 0
        if nota < 1 or nota > 7:
            print("Inserte una nota válida")
        else:
            lista_notas.append(nota)
            estudiantes[nombre] = lista_notas
        return

def calcular_promedios(estudiantes):
    for nombre in estudiantes:
        promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
        promedios_local[nombre] = round(promedio, 2)
    return promedios_local
    
try:
    n_estudiantes = int(input("Ingrese el número de estudiantes"))
    n_notas = int(input("Ingrese el número de notas que desea agregar"))
except ValueError as error:
    print("Error: ", error)
    print("El valor debió haber sido un entero")
    n_estudiantes = 0
    n_notas = 0
if n_estudiantes < 1 or n_notas < 1:
    print("Ingrese un valor apropiado")
else:

    for estudiante in range(n_estudiantes):
        nombre = input("Inserte el nombre\n")
        agregar_estudiantes(estudiantes,nombre)

    calcular_promedios(estudiantes)
    print(estudiantes)
    print(promedios_local)