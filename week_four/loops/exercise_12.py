# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def get_valid_phrase_and_letter():
    def error_msg(criterion):
        print(f'>>> ERROR: INGRESE UNA {criterion} PARA CONTINUAR')

    while True:
        word = input('>>> INGRESE UNA FRASE:\n>>> ')
        if word != '':
            break
        error_msg('FRASE')
        
    while True:
        letter = input('>>> INGRESE UNA LETRA:\n>>> ')
        letter = letter.strip()
        if len(letter) == 1 and letter.isalpha():
            break
        error_msg('LETRA ÚNICA')

    return word, letter

def main():
    word, letter = get_valid_phrase_and_letter()
    number_letter_in_phrase = word.count(letter)
    print(f'>>> LA LETRA "{letter}" APARECE {number_letter_in_phrase} VECES EN LA FRASE')

main()
