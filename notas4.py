'''Ejercicio 4: Registro inteligente de calificaciones
Enunciado:
Crea un programa que permita al usuario ingresar varios registros de estudiantes.
Cada registro debe incluir el nombre del estudiante y una materia con su nota.

Al finalizar, muestra:

Un diccionario donde cada clave es un estudiante, y su valor es otro diccionario con sus materias y notas.
El estudiante con mayor promedio.
La lista de materias cursadas por más de un estudiante.
Salida esperada (ejemplo):

{
  'Ana': {'matemáticas': 6.5, 'historia': 6.8},
  'Luis': {'historia': 5.8},
  'Sofía': {'matemáticas': 7.0}
}

Mejor promedio: Sofía

Materias con más de un estudiante: ['matemáticas', 'historia']

El ingreso de datos termina cuando el usuario escribe "fin" como nombre del estudiante.'''

estudiantes = {}

def agregar_estudiantes():

    while True:
        notas = {}
        nombre = input("Ingrese nombre de estudiante")
        while True:
            asig = input("Ingrese el nombre de la asignatura")
            try:
                promedio = float(input("Ingrese el promedio de la asignatura"))
            except ValueError as error:
                print("Error: ", error)
                print("Se esperaba un real")

            notas[asig] = promedio

            try: 
                yes_no_asig = int(input("Desea agregar otra asignatura?\n1. Sí\n2. No\n"))
            except ValueError as error:
                print("Error: ", error)
                print("Se esperaba un entero")
            if yes_no_asig == 1:
                continue
            elif yes_no_asig == 2:
                break
            else:
                print("Inserte una opción válida")


        estudiantes[nombre] = notas
        try: 
            yes_no_est = int(input("Desea agregar otro estudiantes?\n1. Sí\n2. No\n"))
        except ValueError as error:
            print("Error: ", error)
            print("Se esperaba un entero")
        if yes_no_est == 1:
            continue
        elif yes_no_est == 2:
            break
        else:
            print("Inserte una opción válida")


agregar_estudiantes()
print(estudiantes)
