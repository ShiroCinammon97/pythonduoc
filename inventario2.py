'''
Crea un programa que administre un inventario de productos, donde cada producto tenga:
un nombre
un código (alfanumérico, obligatorio y único)
una categoría
Los datos se deben ingresar de uno en uno, y almacenarse en una lista de diccionarios.

📌 Reglas:
No se permite registrar dos productos con el mismo código.
El programa debe validar que el código tenga al menos 4 caracteres y al menos una letra y un número.
El programa debe permitir al usuario consultar cuántos productos hay por categoría al final.
🔁 El programa termina cuando el usuario escribe "FIN" como nombre de producto.
'''

productos = []

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
        pass
    elif opcion == 3:
        print("Adios")
        break
    elif opcion == 0:
        print("Ingrese un número entero")
    else:
        print("Ingrese una opción válida")