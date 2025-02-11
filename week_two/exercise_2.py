'''
Ejercicio 2: Contador de Vocales y Consonantes

Descripción:

El programa pedirá al usuario que ingrese una frase, y luego deberá contar cuántas vocales y cuántas consonantes hay en la frase. Debe ignorar los espacios y caracteres especiales. Al final, debe mostrar el número de vocales y consonantes.

Requerimientos:

Pedir una cadena de texto (como str).
Contar las vocales y consonantes (usando estructuras de control y cadenas).
Ignorar los espacios y caracteres no alfabéticos (como números y signos de puntuación).
'''

def read_input():
    while True:
        phrase = input('>>> INGRESE UNA FRASE:\n>>> ')
        if phrase != '': return phrase
        print('>>> INGRESE UNA FRASE VÁLIDA')

vowels = str('aáeéiíoóuúü')
consonants = str('bcdfghjklmnñpqrstvwxyz')

vowels_count = consonants_count = 0

phrase = read_input()

for character in phrase:
    if character.isalpha():
        for vowel in vowels:
            if character == vowel: vowels_count += 1
        for consonant in consonants:
            if character == consonant: consonants_count += 1

print(f'>>> {vowels_count} VOCAL(ES)\n>>> {consonants_count} CONSONANTE(S)')
