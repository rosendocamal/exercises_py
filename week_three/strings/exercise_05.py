# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

while True:
    phrase = input('>>> INGRESE UNA FRASE:\n>>> ')
    try:
        if phrase != '':
            break
        else:
            print('>>> INTRODUZCA UNA FRASE PARA CONTINUAR')
    except:
        print('>>> INTRODUZCA UNA FRASE PARA CONTINUAR')

phrase_reverse = list()
for i in phrase:
    phrase_reverse.append(i)
phrase_reverse.reverse()
phrase_reverse = str().join(phrase_reverse)
print(f'>>> {phrase_reverse}')

