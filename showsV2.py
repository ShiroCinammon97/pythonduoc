'''
Inicio del sistema: Registro o Inicio de sesión

Antes de mostrar el menú, el usuario debe elegir entre:
1. Iniciar sesión
2. Registrar nuevo usuario

Registro de usuario:

- El usuario debe ingresar un nombre de usuario único.
- Luego debe crear una contraseña que cumpla las siguientes condiciones:
  - Al menos 9 caracteres
  - Al menos una letra mayúscula
  - Al menos un carácter especial de la lista: ["*", "-", "!", "_", ",", "."]
- Si no se cumplen los requisitos, se muestra un mensaje de error y se vuelve a solicitar la contraseña.

Inicio de sesión:

- Se solicita nombre de usuario y contraseña.
- El usuario debe haber sido registrado previamente.
- Si las credenciales son incorrectas, no se podrá ingresar.

Menú del sistema

*** SISTEMA DE SHOWS EN VIVO ***

1. Mostrar artistas por país
2. Porcentaje de shows en un mes
3. Eliminar artista por nombre
4. Salir

Funcionalidades
1. Artistas por país

- Función: artistas_por_pais(pais)
- Muestra una lista ordenada de artistas que se presentan en el país ingresado.
- Si no hay artistas del país: "No hay artistas de ese país."

2. Porcentaje de shows en un mes

- Función: shows_por_mes(mes)
- Valida que el mes esté entre 1 y 12.
- Devuelve el porcentaje de shows en ese mes (redondeado a un decimal).

3. Eliminar artista por nombre

- Función: eliminar_artista()
- Solicita nombre del artista y lo elimina si existe (sin importar mayúsculas/minúsculas).
- Mensajes posibles:
  - "Artista eliminado con éxito."
  - "Artista no encontrado. No se pudo eliminar."
4. Salir
- Finaliza el programa con el mensaje: "Programa cerrado."
'''

usuarios = {"admin": "Admin*2025"}

shows = {
    "A001": ["Taylor Swift", "Estados Unidos", "15-09-2025"],
    "A002": ["Bad Bunny", "Puerto Rico", "03-08-2025"],
    "A003": ["Rosalía", "España", "21-10-2025"],
    "A004": ["BLACKPINK", "Corea del Sur", "05-07-2025"],
    "A005": ["Dua Lipa", "Reino Unido", "18-08-2025"],
    "A006": ["BTS", "Corea del Sur", "12-09-2025"],
    "A007": ["Shakira", "Colombia", "25-11-2025"],
    "A008": ["Karol G", "Colombia", "02-12-2025"],
    "A009": ["The Weeknd", "Canadá", "30-06-2025"]
} 

login = False
contador_login = 0

def verificar_passwd(passwd):
    upper = False
    caracter = False

    if len(passwd) <= 9:
        return False
    for character in passwd:
        if character.isupper():
            upper = True
        if character == ["x","!","+"]:
            caracter = True
    if not upper:
        return False
    if not caracter:
        return False

def artistas_por_pais(pais):
    pass

def shows_por_mes(mes):
    pass

def eliminar_artista():
    pass

#Sistema de login

while True:
    opcion_login = int(input("Igrese una opcion:\n1. Iniciar sesión\n2. Registrar nuevo usuario\n"))
    if opcion_login == 1:
        while True:
            username = input("Inserte nombre de usuario")
            passwd = input("Inserte contraseña")
            for id in usuarios:
                if passwd == usuarios["admin"]:
                    login = True
            if login == True:
                    print("Acceso concebido")
                    break
            contador_login += 1
            if contador_login == 3:
                break
    elif opcion_login == 2:
            username = input("Inserte nombre de usuario")
            for usuario in usuarios:
                if usuario != username:
                    disponible = True
                    print("Nombre de usuario disponible")

            passwd = input("Inserte contraseña")
            if verificar_passwd(passwd):
                usuarios[username] = passwd
                print("Válido")
            else:
                print("Inválido")
            
            

    else:
        print("Ingrese una opción válida")

#Menu principal
if login == False:
    print("Máximo de intentos de acceso, vuelva a intentarlo en 30 minutos")
else:
    print("*** SISTEMA DE SHOWS EN VIVO ***")
    while True:
        opcion = int(input("Igrese una opcion:\n1. Mostrar artistas por país\n2. Porcentaje de shows en un mes\n3. Eliminar artista por nombre\n4. Salir\n"))

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            print("Adios")
            break
        else:
            print("Ingrese una opción válida")