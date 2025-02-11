# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def is_prime_number(number):
    if number == 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    try:
        number = int(input('>>> INGRESE UN NÚMERO NATURAL MAYOR QUE CERO:\n>>> '))
        if number >= 1:
            if is_prime_number(number):
                print(f'>>> EL NÚMERO {number} ES PRIMO')
            else:
                print(f'>>> EL NÚMERO {number} NO ES PRIMO')
            print('>>> EL PROGRAMA HA FINALIZADO')
            break
        else:
            print('>>> ERROR: INGRESE UN NÚMERO ENTERO MAYOR A CERO')
    except ValueError:
        print('>>> ERROR: POR FAVOR INGRESE UN NÚMERO ENTERO VÁLIDO MAYOR A CERO')
