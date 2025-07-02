'''
🏫 Ejercicio: Sistema de Registro de Asistencia Escolar
Un colegio necesita un sistema simple para llevar la asistencia de estudiantes de una sola clase.

Cada estudiante está representado por un diccionario con los siguientes datos:

{
    "nombre": "Carlos",
    "asistencias": [True, False, True]  # True = asistió, False = ausente
}
El programa debe funcionar mediante un menú interactivo con while True que ofrezca las siguientes opciones:

📋 Menú principal:

1. Agregar estudiante  
2. Registrar asistencia  
3. Ver asistencias de un estudiante  
4. Ver lista de estudiantes con más del 75% de asistencia  
5. Salir

🧩 Reglas:
Al agregar un estudiante, se inicia con la lista de asistencias vacía.
Al registrar asistencia, se itera sobre todos los estudiantes preguntando si asistió (s para sí, cualquier otra cosa es no).
Para calcular porcentaje: (asistencias positivas / total de registros) * 100
Si aún no tiene asistencias, su porcentaje no debe dividir por cero.
'''

def agregar_estudiante():
    pass
def registrar_asistencia():
    pass
def ver_asistencia():
    pass
def asistencia_aprobados():
    pass

while True:
    try:
        opcion = int(input("Ingrese una opción:\n1. Agregar estudiante\n2. Registrar asistencia\n3. Ver asistencias de un estudiante\n4. Ver lista de estudiantes con más del 75% de asistencia\n5. Salir"))
    except ValueError as error:
        print("Error: ", error)
        print("Se esperaba un valor entero")
    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        registrar_asistencia()
    elif opcion == 3:
        ver_asistencia()
    elif opcion == 4:
        asistencia_aprobados()
    elif opcion == 5:
        print("Adios")
        break
    else:
        print("Inserte una opción válida")