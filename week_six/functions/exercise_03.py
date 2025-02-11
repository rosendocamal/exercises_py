# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def get_int():
    while True:
        try:
            int_num = int(input('>>> INGRESE UN NÚMERO ENTERO MAYOR O IGUAL A CERO:\n>>> '))
            if int_num >= 0:
                return int_num
            else:
                print('>>> ERROR: PARA EL FACTORIAL SE DEBE INGRESAR UN NÚMERO MAYOR O IGUAL A CERO')
        except ValueError:
            print('>>> ERROR: POR FAVOR, INGRESE ALGÚN NÚMERO VÁLIDO PARA CONTINUAR')

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def main():
    int_num = get_int()
    factorial_n = factorial(int_num)
    print(f'>>> {factorial_n}')

if __name__ == '__main__':
    main()
