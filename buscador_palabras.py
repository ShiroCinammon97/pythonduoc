'''
🔍 Ejercicio: Buscador de palabras y sus posiciones
Escribe un programa que reciba una frase del usuario y luego permita buscar varias palabras dentro de esa frase. El programa debe indicar en qué posiciones (índices) aparecen esas palabras dentro de la frase (considerando las palabras como una lista).

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

🧪 Ejemplo de uso esperado:
Frase ingresada:

arduino
Copy
Edit
"la casa es grande y la casa es blanca"
Palabras a buscar:

css
Copy
Edit
["casa", "es", "blanca"]
Salida esperada:

css
Copy
Edit
casa → [1, 6]
es → [2, 7]
blanca → [8]
'''