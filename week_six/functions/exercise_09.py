# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def get_leas_common_multiple(a, b):
    factor = 0
    while b > 0:
        factor = b
        b = a % b
        a = factor
    return factor
        

def get_greatest_common_divisor(a=1, b=1):
    divisor = a if a >= b else b
    while True:
        x, y = a % divisor, b % divisor
        if x == y and x == 0:
            return divisor
        divisor -= 1

def main():
    def get_number():
        while True:
            try:
                num = int(input('>>> INGRESE UN NÚMERO ENTERO MAYOR QUE 0:\n>>> '))
                if num > 0:
                    return num
                else:
                    print('>>> ERROR: INTRODUCE UN NÚMERO VÁLIDO MAYOR QUE 0')
            except ValueError:
                print('>>> ERROR: POR FAVOR, INGRESE UN NÚMERO VÁLIDO PARA CONTINUAR')
    
    num_a, num_b = get_number(), get_number()

    gcd = get_greatest_common_divisor(num_a, num_b)
    gcf = get_leas_common_multiple(num_a, num_b)

    return f'>>> MÍNIMO COMÚN MÚLTIPLO: {gcf}\n>>> MÁXIMO COMÚN DIVISOR: {gcf}'

print(main())


