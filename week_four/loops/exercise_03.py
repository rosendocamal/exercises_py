# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.G

def is_odd_number(number):
    if number % 2 != 0:
        return True
    return False

def print_list_odd_number(input_number):
    list_odd_number = []
    for i in range(input_number):
        if is_odd_number(i + 1):
            list_odd_number.append(i + 1)
    return [str(item) for item in list_odd_number]
    

def read_input():
    while True:
        try:
            input_number = int(input('>>> INGRESE UN NÚMERO NATURAL:\n>>> '))
            if 1 <= input_number:
                return input_number
            else:
                print('>>> ERROR: INGRESE UN NÚMERO ENTERO MAYOR QUE CERO')
        except ValueError:
            print('>>> ERROR: INGRESE UN NÚMERO ENTERO PARA CONTINUAR')

def main():
    input_number = read_input()
    odd_numbers = print_list_odd_number(input_number)
    print(', '.join(odd_numbers))

if __name__ == '__main__':
    main()
