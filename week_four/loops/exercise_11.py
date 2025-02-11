# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def read_input():
    while True:
        try:
            word = input('>>> INGRESE UNA PALABRA:\n>>> ')
            if word.isalpha():
                return word
            else:
                print('>>> ERROR: INGRESE ÚNICAMENTE UNA PALABRA')
        except ValueError:
            print('>>> ERROR: POR FAVOR, INGRESE ÚNICAMENTE UNA PALABRA')

def main():
    inverted_word = read_input()[::-1]
    for character in inverted_word:
        print(f'>>> {character}')
    print('>>> EL PROGRAMA HA FINALIZADO CON ÉXITO')

main()
