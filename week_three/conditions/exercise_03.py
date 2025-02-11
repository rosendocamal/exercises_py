# Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

while True:
    try:
        dividend = float(input('>>> INGRESE UN DIVIDENDO:\n>>> '))
        break
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO COMO DIVIDENDO')

while True:
    try:
        divisor = float(input('>>> INGRESE UN DIVISOR:\n>>> '))
        if divisor != 0:
            break
        else:
            print('>>> ERROR: NO SE PUEDE DIVIDIR ENTRE CERO. ASIGNE UN NÚMERO DISTINTO COMO DIVISOR')
    except ValueError:
        print('>>> INGRESE UN NÚMERO COMO DIVISOR')

print(f'>>> {dividend} ÷ {divisor} = {dividend / divisor}')
