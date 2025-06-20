'''
Ejercicio: Analizador de palabras únicas por usuario
Tienes una lista de mensajes enviados por distintos usuarios en una plataforma. Cada mensaje tiene:

un "usuario" (nombre del usuario que lo escribió)

un "mensaje" (texto del mensaje)

✏️ Tarea:
Crea una función palabras_unicas_por_usuario(mensajes) que reciba una lista de diccionarios como este:

python
Copy
Edit

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
        if clave["usuario"] == "Ana":
            frase_ana = clave["mensaje"].split(" ")
            #mensajes_ana.append(clave["mensaje"])
        if clave["usuario"] == "Luis":
            frase_luis = clave["mensaje"].split(" ")
            #mensajes_luis.append(clave["mensaje"])
    
    for clave in frase_ana:
        if clave not in mensajes_ana:
            mensajes_ana.append(clave)

    for clave in frase_luis:
        if clave not in mensajes_luis:
            mensajes_luis.append(clave)

    for clave in mensajes:
        if clave["usuario"] not in mensajes_por_usuario:
            if clave["usuario"] == "Ana":
                mensajes_por_usuario["Ana"] = mensajes_ana
            if clave["usuario"] == "Luis":
                mensajes_por_usuario["Luis"] = mensajes_luis
    print(mensajes_por_usuario)

palabras_unicas_por_usuario(mensajes)

