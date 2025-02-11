'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
'''

while True:
    try:
        number = int(input('>>> INGRESE UN NÚMERO ENTERO:\n>>> '))
        if number >= 1:
            pattern = '*'
            for i in range(number):
                print(f'>>> {pattern * (i + 1)}')
            print('>>> EL PATRÓN SE HA GENERADO CON ÉXITO')
            break
        else:
            print('>>> ERROR: INGRESE UN NÚMERO VÁLIDO MAYOR QUE CERO')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO ENTERO VÁLIDO')
