'''
🧠 Ejercicio: Control de acceso con intentos y bloqueo
Crea un sistema de acceso de usuarios. Cada usuario tiene:
usuario (nombre de usuario)
clave (contraseña)
intentos (inicia en 0)
bloqueado (True o False)

Los usuarios están en una lista de diccionarios. El sistema debe permitir al usuario intentar iniciar sesión. Si falla 3 veces, el usuario se bloquea automáticamente.

📋 Reglas:
Si el usuario no existe, mostrar mensaje de error.
Si el usuario está bloqueado, denegar acceso inmediatamente.
Si la clave es incorrecta, aumentar el contador de intentos.
Al tercer intento fallido, bloquear al usuario.

Si la clave es correcta y el usuario no está bloqueado, dar acceso y reiniciar los intentos.
'''

intentos = 0
bloqueado = False
usuarios = {"Usuario":"admin","Contraseña":"User_1234"}

def verificar_usuario(nombre_usuario,passwd):
    if nombre_usuario == usuarios["Usuario"]:
        if passwd == usuarios["Contraseña"]:
            return True

while True:
    nombre_usuario = input("Inserte el nombre de usuario\n")
    passwd = input("Inserte la contraseña\n")
    if verificar_usuario(nombre_usuario,passwd):
        intentos = 0
        break
    else:
        print("Error: Usuario y/o contraseña no válidos")
        intentos += 1
        print("Le quedan: ",3-intentos," intentos")

    if intentos == 3:
        bloqueado = True
        break

if bloqueado == True:
    print("Usuario bloqueado, contacte a su administrador")
else:
    print("Bienvenido al programa")