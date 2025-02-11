'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
def print_triangule(number):
    for i in range(1, number + 1, 2):
        print('>>>', end=' ')
        for j in range(i, 0, -2):
            print(j, end=' ')
        print('')
    print('>>> EL TRIÁNGULO HA SIDO GENERADO CON ÉXITO')

while True:
    try:
        number = int(input('>>> INGRESE UN NÚMERO NATURAL:\n>>> '))
        if number >= 1:
            print_triangule(number)
            break
        else:
            print('>>> ERROR: INGRESE UN NÚMERO ENTERO MAYOR QUE CERO')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO ENTERO VÁLIDO')
