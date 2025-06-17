'''Ejercicio 1: agregar estudiantes y sus calificaciones a un diccionario
Crea un programa que permita agregar nombres de estudiantes como claves y sus calificaciones como valores en un diccionario. Luego, imprime el diccionario.'''

notas = {}

try:
    n_estudiante = int(input("Cuantos quiere agregar?\n"))
except ValueError as error:
    print("Error: ",error)
    print("Debió haber agregado un valor entero")
    n_estudiante = -1
if n_estudiante < 0:
    print("Inserte una opción válida")
else:
    for estudiante in range(n_estudiante):
        nombre = input("Ingrese el nombre del estudiante\n")
        nota = float(input("Ingrese su nota\n"))
        notas[nombre] = nota

print(notas)
