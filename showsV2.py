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

print(shows)