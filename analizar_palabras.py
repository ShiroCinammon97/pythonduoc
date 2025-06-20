'''
Ejercicio: Analizador de palabras únicas por usuario
Tienes una lista de mensajes enviados por distintos usuarios en una plataforma. Cada mensaje tiene:

un "usuario" (nombre del usuario que lo escribió)

un "mensaje" (texto del mensaje)

✏️ Tarea:
Crea una función palabras_unicas_por_usuario(mensajes) que reciba una lista de diccionarios como este:


La función debe devolver un diccionario donde cada clave sea un usuario, y su valor sea un conjunto de palabras únicas que ese usuario ha escrito en todos sus mensajes.

✅ Resultado esperado (sin usar set() explícitamente, pero puedes construir la lógica):
python

{
    "Ana": ["hola", "cómo", "estás", "todo", "bien", "gracias"],
    "Luis": ["hola", "Ana", "bien", "y", "tú"]
}
'''
mensajes = [
    {"usuario": "Ana", "mensaje": "hola Hola cómo estás"},
    {"usuario": "Luis", "mensaje": "hola Ana bien y tú"},
    {"usuario": "Ana", "mensaje": "todo bien gracias"},
]

def palabras_unicas_por_usuario(mensajes):
    mensajes_por_usuario = {}
    mensajes_ana = []
    mensajes_luis = []

    for clave in mensajes:
        usuario = clave["usuario"]
        frase = clave["mensaje"].split(" ")

        # Inicializar la lista si el usuario no está aún
        if usuario not in mensajes_por_usuario:
            mensajes_por_usuario[usuario] = []

        # Agregar palabras si no están repetidas
        for palabra in frase:
            if palabra not in mensajes_por_usuario[usuario]:
                mensajes_por_usuario[usuario].append(palabra)

    print(mensajes_por_usuario)

palabras_unicas_por_usuario(mensajes)

