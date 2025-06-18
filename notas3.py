''' 
Ejercicio: Sistema de gestión de cursos y estudiantes
Crea un programa que gestione una lista de cursos. Cada curso tiene un grupo de estudiantes, y cada estudiante tiene varias calificaciones. 
El programa debe permitir registrar esta información, calcular promedios individuales por estudiante, y mostrar resúmenes por curso.

🎯 Objetivos:
Registrar varios cursos, cada uno con su lista de estudiantes.
Para cada estudiante, registrar su nombre y sus notas (3 calificaciones).
Calcular el promedio de cada estudiante.
Mostrar un resumen por curso: estudiantes con sus promedios, y el promedio general del curso.

🧾 Requisitos y funciones sugeridas:
agregar_estudiante()
Recibe una lista vacía de estudiantes y agrega diccionarios del tipo:
{"nombre": "Juan", "notas": [8, 7, 9]}.
agregar_curso()
Recibe un diccionario de cursos. Pide el nombre del curso y una cantidad de estudiantes, y llama a agregar_estudiante() para registrar cada uno.
calcular_promedios_estudiantes()
Para cada estudiante, calcula su promedio y lo agrega al diccionario del estudiante bajo la clave "promedio".
resumen_curso()
Muestra todos los estudiantes con sus promedios.
Calcula y muestra el promedio general del curso.
'''

curso = []


def agregar_estudiante():
    lista_notas = []
    for nota in range(3):
        nota = float(input("Ingrese nota"))
        lista_notas.append(nota)
    dict_estudiante["nota"] = lista_notas
    
def calcular_promedios_estudiantes():
    promedios_estudiantes = {}
    for estudiante in curso:
        promedio = sum(estudiante["nota"])/len(estudiante["nota"])
        promedios_estudiantes[estudiante["nombre"]] = round(promedio, 2)
    return promedios_estudiantes

#def resumen_curso():


for estudiante in range(3):
    dict_estudiante = {}
    nombre_estudiante = input("Ingrese nombre del estudiante\n")
    dict_estudiante["nombre"] = nombre_estudiante
    agregar_estudiante()
    curso.append(dict_estudiante)

promedio_cada_uno = calcular_promedios_estudiantes()

print(curso)
print(promedio_cada_uno)
