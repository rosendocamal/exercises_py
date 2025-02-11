def entry_division():
    def get_number(type_num):
        while True:
            try:
                num = float(input(f'INGRESE UN {type_num}:\n'))
                if type_num == 'DIVISOR' and num == 0:
                    print('NO SE PUEDE DIVIDIR ENTRE CERO. INGRESE CUALQUIER OTRO NÚMERO COMO DIVISOR')
                else:
                    return num
            except ValueError:
                print('POR FAVOR, INGRESE UN NÚMERO VÁLIDO PARA CONTINUAR')

    a = get_number('DIVIDENDO')
    b = get_number('DIVISOR')
    return a, b

def division():
    dividend, divisor = entry_division()
    quotient = dividend / divisor
    print(f'{dividend} / {divisor} = {quotient}')

division()
