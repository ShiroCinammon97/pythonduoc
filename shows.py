'''
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

def inicio_sesion():
    pass

def artistas_por_pais():
    pass

def shows_por_mes():
    pass

def eliminar_artista():
    pass

for id in shows:
    print(id)
