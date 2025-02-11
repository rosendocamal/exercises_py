# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

winning_numbers = [0, 0, 0, 0, 0, 0]

for i in range(len(winning_numbers)):
    while True:
        try:
            winning_number = int(input('INTRODUCE EL NÚMERO GANADOR:\n'))
            if 1 <= winning_number <= 49:
                if winning_numbers.count(winning_number) == 0:
                    winning_numbers[i] = winning_number
                    break
                else:
                    print(f'ERROR: EL NÚMERO {winning_number} YA HA SIDO SELECCIONADO')
            else:
                print('ERROR: LOS NÚMEROS GANADORES ESTÁN EN EL RANGO DE 1 Y 49')
        except ValueError:
            print('ERROR: INGRESE UN NÚMERO VÁLIDO GANADOR')

winning_numbers.sort()
print(f'LOS NÚMEROS GANADORES SON {winning_numbers}')
