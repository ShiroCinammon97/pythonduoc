'''
Ejercicio: Rastreador de Errores en Código Fuente
Tienes una lista de diccionarios llamada codigo, donde cada diccionario representa una línea de código de un archivo. Cada diccionario tiene dos claves:

"linea": el contenido de la línea (string),

"estado": puede ser "ok" o "error".

Tu misión es encontrar los índices de las líneas que tienen estado "error", pero solo si están inmediatamente seguidas de otra línea "ok" (es decir, hay una posible corrección justo después).

Crea una lista errores_corrigibles que contenga los índices de esas líneas.
'''

