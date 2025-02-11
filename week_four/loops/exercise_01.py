# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

while True:
    word = input('>>> INGRESA UNA PALABRA:\n>>> ')
    if word != '':
        print('>>>')
        break
    else:
        print('>>> ERROR: INGRESE UNA PALABRA VÁLIDA PARA CONTINUAR')

for i in range(1, 11, 1):
    if i < 10:
        print(f'>>> 0{i}. {word}')
    else:
        print(f'>>> {i}. {word}')
