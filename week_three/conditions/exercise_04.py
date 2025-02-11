# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def get_number(msg, msg_error):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            print(msg_error)

number = get_number('>>> INGRESE UN NÚMERO ENTERO:\n>>> ', '>>> ERROR: INGRESE UN NÚMERO ENTERO VÁLIDO')

if number % 2 == 0:
    print(f'>>> EL NÚMERO {number} ES PAR')
else:
    print(f'>>> EL NÚMERO {number} ES IMPAR')
