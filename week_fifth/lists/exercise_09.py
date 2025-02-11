# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

def get_word():
    while True:
        word = input('>>> INGRESE UNA PALABRA:\n>>> ').strip().lower()
        if word and word.isalpha():
            return word
        else:
            print('>>> ERROR: POR FAVOR, INGRESE ÚNICAMENTE UNA PALABRA VÁLIDA')

def get_number_vowels(word):
    number_vowels = [0, 0, 0, 0, 0]

    for character in word:
        if character == 'a' or character == 'á':
            number_vowels[0] += 1
        elif character == 'e' or character == 'é':
            number_vowels[1] += 1
        elif character == 'i' or character == 'í':
            number_vowels[2] += 1 
        elif character == 'o' or character == 'ó':
            number_vowels[3] += 1
        elif character == 'u' or character == 'ú' or character == 'ü':
            number_vowels[4] += 1

    return number_vowels

def main():
    word = get_word()
    number_vowels = get_number_vowels(word)

    print(f'>>> LA PALABRA "{word.upper()}" CONTIENE LA VOCAL "A" {number_vowels[0]} VECES, LA VOCAL "E" {number_vowels[1]} VECES, LA VOCAL "I" {number_vowels[2]} VECES, LA VOCAL "O" {number_vowels[3]} VECES Y LA VOCAL "U" {number_vowels[4]} VECES')

if __name__ == '__main__':
    main()
