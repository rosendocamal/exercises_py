# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def get_word():
    while True:
        word = input('>>> INGRESE UNA PALABRA:\n>>> ').strip()
        if word != '' and word.isalpha():
            return word.upper()
        else:
            print('>>> ERROR: INGRESE ÚNICAMENTE UNA PALABRA VÁLIDA')

def is_palindrome(word):
    if word[::-1] == word:
        return True
    return False

def main():
    word = get_word()

    def show_msg(word, txt):
        print(f'>>> LA PALABRA "{word}" {txt.upper()} PALÍNDROMA')

    if is_palindrome(word):
        show_msg(word, 'ES')
    else:
        show_msg(word, 'NO ES')


if __name__ == '__main__':
    main()
