# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def print_multiply_table(start, end):
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            print(f'{i * j:03d}', end='\t')
        print('')

print_multiply_table(1, 10)
