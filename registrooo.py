'''
🔹 Ejercicio 4: Registro dinámico de pedidos y consolidación por cliente
Enunciado:

Crea un programa que permita al usuario ingresar múltiples pedidos en formato:

cliente:producto

El usuario puede ingresar todos los pedidos que desee, uno por línea.
Cuando escriba "fin", el programa dejará de pedir entradas.
Luego, muestra un diccionario donde las claves son los nombres de los clientes 
y los valores son listas de productos que pidió cada uno, en orden.

Ejemplo de entrada:

Ana:laptop  
Luis:monitor  
Ana:teclado  
Sofía:laptop  
fin


Salida esperada:

{
  "Ana": ["laptop", "teclado"],
  "Luis": ["monitor"],
  "Sofía": ["laptop"]
}
'''

lista_pedidos = []

def ingresar_pedidos():
    pedidos = []
    cliente = input("Ingrese el nombre del cliente\n")

    while True:
        pedido = input("Ingrese que producto quiere de pedido\n")
        pedidos.append(pedido)
        try:
            yes_no = int(input("Desea ingresar otro producto?\n1. Sí\n2. No\n"))
        except ValueError as error:
            print("Error: ", error)
            print("Se esperaba un entero")
        if yes_no == 1:
            continue
        elif yes_no == 2:
            break
        else:
            print("Ingrese una opción válida")
    lista_pedidos.append({"cliente":cliente,"pedidos":pedidos})

while True:
    try:
        opcion = int(input("Qué desea hacer?\n1. Agregar pedidos?\n2. Mostrar lista de pedidos\n3. Salir\n"))
    except ValueError as error:
        print("Error: ",error)
        print("Se esperaba un número entero")
        continue
    if opcion == 1:
        ingresar_pedidos()
    elif opcion == 2:
        print(lista_pedidos)
    elif opcion == 3:
        print("adios")
        break
    else:
        print("Inserte una opción válida")