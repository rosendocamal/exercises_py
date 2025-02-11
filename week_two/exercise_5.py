'''
Ejercicio 5: Anagramas

Descripción:

Crea una función que determine si dos palabras o frases ingresadas por el usuario son anagramas, es decir, si están formadas por las mismas letras, aunque estén en diferente orden. El programa debe ignorar los espacios y las mayúsculas.

Requerimientos:

El programa debe comparar las palabras o frases después de normalizarlas (convertir a minúsculas y eliminar espacios).
Utiliza los métodos de cadenas y listas para comparar las letras de ambas entradas.
Ejemplo de entrada: "listen" y "silent" → "Son anagramas".
'''

def read_input():
    while True:
        word_or_phrase = [str(), str()]

        msg = str('>>> INGRESE UNA PALABRA O FRASE:\n>>> ')
        word_or_phrase[0], word_or_phrase[1] = input(f'{msg}'), input(f'{msg}')

        if word_or_phrase[0] != str() and word_or_phrase[1] != str(): return word_or_phrase
        print('>>> INGRESE UNA PALABRA O FRASE VÁLIDA PARA CONTINUAR')

input_data = read_input()
work_data = [[[], []], [[], []]]

work_data[0][0], work_data[0][1] = ''.join(input_data[0].split()).lower(), ''.join(input_data[1].split()).lower()

for character in work_data[0][0]:
    if character.isalpha() == True:
        work_data[1][0].append(character)
for character in work_data[0][1]:
    if character.isalpha() == True:
        work_data[1][1].append(character)

work_data[1][0].sort()
work_data[1][1].sort()

if work_data[1][0] == work_data[1][1]:
    print('>>> SON ANAGRAMAS')
else:
    print('>>> NO SON ANAGRAMAS')
