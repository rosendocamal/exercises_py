'''
Ejercicio 3: Palíndromos

Descripción:

Crea un programa que verifique si una palabra o frase ingresada por el usuario es un palíndromo, es decir, si se lee igual de adelante hacia atrás (ignorando espacios, mayúsculas y minúsculas). El programa debe devolver un mensaje indicando si la entrada es un palíndromo o no.

Requerimientos:

El programa debe eliminar espacios y convertir todos los caracteres a minúsculas.
Utiliza métodos de cadenas y listas para comparar el texto original con su reverso.
Ejemplo de entrada: "A man a plan a canal Panama" → "Es un palíndromo".
'''

def read_input():
    while True:
        word_or_phrase = input('>>> INGRESE UNA PALABRA O UNA FRASE:\n>>> ')
        if word_or_phrase != str(''): return word_or_phrase
        print('>>> INGRESE UNA PALABRA O FRASE VÁLIDA PARA CONTINUAR')

data_string, similar_characters = str().join(read_input().split()).lower(), 0

for i in range(0, len(data_string), 1):
    if data_string[i] == data_string[len(data_string) - (1 + i)]: similar_characters += 1

print('ES UN PALÍNDROMO') if similar_characters == len(data_string) else print('NO ES PALÍNDROMO')
