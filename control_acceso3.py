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
productos = []

usuarios = [
    {"usuario": "ana", "clave": "1234"},
    {"usuario": "luis", "clave": "luispass"}
]

def verificar_usuario(nombre_usuario,passwd):
    for usuario in usuarios:
        if nombre_usuario == usuario["usuario"]:
            if passwd == usuario["clave"]:
                return True
            
def verificar_codigo(codigo):
    num = False
    letra = False
    if len(productos) == 0:
        pass
    else:
        for producto in productos:
            if producto["Código"] == codigo:
                print("Código ya existe")
                return False
    
    if len(codigo) < 4:
        print("El código debe ser de almenos 4 caracteres")
        return False
    
    for caracter in codigo:
        if caracter.isnumeric():
            num = True
        if caracter.isalpha():
            letra = True
    
    if num == True and letra == True:
        return True
    else:
        print("El código debe tener almenos una letra y un número")
        return False

def agregar_producto(nombre,codigo,categoria):
    productos.append({"Nombre":nombre,"Código":codigo,"Categoría":categoria})


def mostrar_por_categoria(categoria,productos):
    categorias_individuales = {}

    for producto in productos:
        categoria = producto["Categoría"]
        if categoria in categorias_individuales:
            categorias_individuales[categoria] += 1
        else:
            categorias_individuales[categoria] = 1
    #for categoria, cantidad in categorias_individuales.items():
    print(categorias_individuales)

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
    while True:
        try:
            opcion = int(input("Inserte una opcion:\n1. Agregar Producto\n2. Ver Productos por categoría\n3. Salir\n"))
        except ValueError as error:
            print("Error: ",error)
            print("Se esperaba un número entero")
            opcion = 0
        if opcion == 1:
            nombre = input("Inserte el nombre del producto\n")
            while True:
                codigo = input("Inserte el código del producto\n")
                if verificar_codigo(codigo) == True:
                    break
            categoria = input("Inserte el categoría del producto\n")
            agregar_producto(nombre,codigo,categoria)
        elif opcion == 2:
            mostrar_por_categoria(categoria,productos)
        elif opcion == 3:
            print("Adios")
            break
        elif opcion == 0:
            print("Ingrese un número entero")
        else:
            print("Ingrese una opción válida")