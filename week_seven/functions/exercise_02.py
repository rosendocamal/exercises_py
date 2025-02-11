# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

from math import sin, cos, tan, exp, log

def apply_function(function, num):
    functions = {'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log}
    result = {i: functions[function](i) for i in range(1, num + 1)}
    return result

def request_entry(msg):
    return input(msg)

def is_valid_function_option(option):
    return option in ['sin', 'cos', 'tan', 'exp', 'log']

def is_positive_int(option):
    try:
        option = int(option)
        return option >= 0
    except ValueError:
        return False

def request_valid_entry(msg, validator):
    entry = request_entry(msg)
    if validator(entry):
        return entry
    else:
        print('>>> REINTENTE DE NUEVO')
        return request_valid_entry(msg, validator)

def calculator():
    f = request_valid_entry('>>> INGRESE UNA OPERACIÓN A REALIZAR (sin, cos, tan, exp, log):\n>>> ', is_valid_function_option)
    n = int(request_valid_entry('>>> INGRESE UN NÚMERO ENTERO POSITIVO:\n>>> ', is_positive_int))
    for i, j in apply_function(f, n).items():
        print(f'>>> {i}\t{j}')

calculator()
