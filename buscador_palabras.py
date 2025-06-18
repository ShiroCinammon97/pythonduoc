'''
🔍 Ejercicio: Buscador de palabras y sus posiciones
Escribe un programa que reciba una frase del usuario y luego permita buscar varias palabras dentro de esa frase. 
El programa debe indicar en qué posiciones (índices) aparecen esas palabras dentro de la frase 
(considerando las palabras como una lista).

🎯 Objetivos del ejercicio:
Convertir una frase en una lista de palabras.
Permitir buscar varias palabras en esa lista.
Indicar en qué índices se encuentra cada palabra (puede haber repeticiones).
Mostrar un resumen con los resultados en forma de diccionario.

🧾 Funciones sugeridas:
dividir_frase(frase)
→ Convierte una frase en una lista de palabras.
buscar_indices(palabras, objetivo)
→ Devuelve una lista con los índices en los que aparece la palabra objetivo.
buscar_varias(palabras, lista_busqueda)
→ Devuelve un diccionario donde la clave es la palabra buscada y el valor es la lista de índices donde aparece.
mostrar_resultados(resultados)
→ Imprime cada palabra junto con las posiciones donde aparece.
'''

lista_busqueda = []

def dividir_frase(frase):
    palabras = frase.split(" ")
    return palabras

def buscar_indices(palabras, objetivo):
    for iindice, palabra in enumerate(palabras):
        if objetivo == palabra:
            return iindice

def buscar_varias(palabras, lista_busqueda):
    pass
        

frase = input("Inserte una frase\n")
palabras = dividir_frase(frase)
objetivo = input("Qué palabra quiere consultar?")
indice_palabra = buscar_indices(palabras, objetivo)
print(indice_palabra)

#print(frase_dividida)