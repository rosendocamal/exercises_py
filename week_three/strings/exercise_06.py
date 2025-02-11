# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def msg_error(name):
    return str(f'>>> INTRODUZCA UNA {name} PARA CONTINUAR')

while True:
    phrase = input('>>> INGRESE UNA FRASE:\n>>> ')
    if phrase != '':
        break
    else:
        print(msg_error('FRASE'))

while True:
    vowel = input('>>> INGRESE UNA VOCAL:\n>>> ')
    if vowel != '' and vowel.lower() in 'aeiou':
        break
    else:
        print(msg_error('VOCAL'))

phrase_modify = str()

for character in phrase:
    if character.lower() == vowel.lower():
        phrase_modify += character.upper()
    if character.lower() != vowel.lower():
        phrase_modify += character

print(f'>>> {phrase_modify}')
