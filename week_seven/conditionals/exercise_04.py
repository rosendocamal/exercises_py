def is_odd_num(num):
    def show_msg(num, condition):
        print(f'EL {num} ES NÚMERO {condition}')
    if (num / 2) - round(num / 2, 0) == 0:
        show_msg(num, 'PAR')
    else:
        show_msg(num, 'IMPAR')

is_not_finish = True
while is_not_finish:
    try:
        num = int(input('INGRESE UN NÚMERO ENTERO:\n'))
        is_odd_num(num)
    except ValueError:
        print('INGRESE UN NÚMERO ENTERO VÁLIDO')
    finally:
        entry_continue = input('DESEA CONTINUAR CON EL PROGRAMA [Y/N]: ').strip().upper()
        if entry_continue == 'Y' or entry_continue == '':
            pass
        else:
            is_not_finish = False

