'''
inicio sesion
 -Se solicita nombre de usuario y contraseña.
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

 Mensajes posibles:
- "Artista eliminado con éxito."
- "Artista no encontrado. No se pudo eliminar."

'''
login = False
contador_login = 0
disponible = True

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

def verificar_passwd (texto):
    upper = False
    char = False
    if len(texto) < 9:
        print("Contraseña debe contener 9 o más caracteres")
        return False
    for caracter in texto:
        if caracter.isupper():
            upper = True
        if caracter in ["*","-","+","!",".",","]:
            char = True
    if not upper:
        print("La contraseña debe contener almenos una mayúscula")
        return False
    if not char:
        print("La contraseña debe contener almenos un caracter especial")
        return False
    

def artistas_por_pais(pais):
    se_presentan = []
    for id in shows:
        if pais == shows[id][1]:
            se_presentan.append(shows[id][0])
        if len(se_presentan) == 0:
            print("No se presentan artistas de ese país")
        else:
            for artista in se_presentan:
                print(artista)

def shows_por_mes(mes):
    largo = 0
    show_mes = 0
    for id in shows:
        fecha = shows[id][1].split("-")
        if int(fecha[1][0]) == 0:
            int(fecha[1][1]) == mes:
                show_mes += 1
        else:
            if int(fecha)            

def eliminar_artista():
    pass

'''for id in shows:
    print(shows[id][0])'''


print("Bienvenido al sistema conciertos")

while True:
    opcion_login = int(input("Inserte opción:1.Login2.Registro"))
    if opcion_login == 1:
        while True:
            usuario = input("Inserte nombre de usuario")
            contrasena = input("Inserte contraseña de usuario")
            for usuario in usuarios:
                if usuarios[usuario] == contrasena:
                    login = True
                else:
                    print("Credenciales incorrectas")
            contador_login += 1
            if login == True:
                print("Bienvenido")
                break
            if contador_login == 3:
                break
        break
    elif opcion_login == 2:
        while True:
            usuario = input("Registrar nombre de usuario")
            for usuario in usuarios:
                disponible = False
            if disponible == False:
                print("Nombre de usuario no disponible")
            else:
                print("Nombre de usuario disponible")
                break
        contrasena = input("Registrar contraseña de usuario")
        verificar_passwd(contrasena)
        if verificar_passwd(contrasena):
            print("Correcto")
            usuarios[usuario] = contrasena
        else:
            print("Incorrecto")
    else:
        print("Inserte opción válida")

if login == False:
    print("Cuenta bloqueada")
else:
    while True:
        opcion = int(input("Ingrese opción\n1. Mostrar artistas por país\n2. Porcentaje de shows en un mes\n3. Eliminar artista por nombre\n4. Salir\n"))
        if opcion == 1:
            pais = input("Inserte un país")
            artistas_por_pais(pais)
        elif opcion == 2:
            mes = int(input("Ingrese un mes (1 a 12):"))
            if mes >= 1 and mes <= 12:
                shows_por_mes(mes)
            else:
                print("Valor invalido")
        elif opcion == 3:
            eliminar_artista()
        elif opcion == 4:
            print("Adios")
            break
        else:
            print("inserte opción váldia")