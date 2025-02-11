# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: \mbox{suma} = \frac{n(n+1)}{2}

def read_input():
    while True:
        try:
            return int(input('>>> INGRESE UN NÚMERO ENTERO POSITIVO:\n>>> '))
        except:
            print('>>> INGRESE UN NÚMERO ENTERO POSITIVO VÁLIDO')

n = read_input()
addition = int((n * (n + 1)) / 2)
print(addition)
