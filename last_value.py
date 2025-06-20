'''
🧩 Ejercicio: Último valor por clave
Dada una lista de diccionarios, cada uno con claves que pueden repetirse en otros diccionarios,
 crea una función que devuelva un nuevo diccionario que contenga el último valor visto para cada clave en la lista.

🔢 Ejemplo de entrada:
python
Copy
Edit
datos = [
    {"a": 1, "b": 2},
    {"b": 3, "c": 4},
    {"a": 5, "d": 6}
]
✅ Salida esperada:
python
Copy
Edit
{
    "a": 5,
    "b": 3,
    "c": 4,
    "d": 6
}
🎯 Objetivo:
Implementa una función como:

python
Copy
Edit
def ultimo_valor_por_clave(lista_diccionarios):
    # tu código aquí


'''

datos = [
    {"a": 1, "b": 2},
    {"b": 3, "c": 4},
    {"a": 5, "d": 6}
]

def ult_val(datos):
    for clave in datos:
        last_key = datos[-1]
    print(last_key)

ult_val(datos)