# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

import math

def first_operand():
    while True:
        try:
            return int(input('>>> INGRESE UN NÚMERO NATURAL COMO DIVIDENDO:\n>>> '))
        except:
            print('>>> INGRESE UN NÚMERO NATURAL PARA CONTINUAR')
            

def second_operand():
    msg = '>>> INGRESE UN NÚMERO MAYOR A CERO'
    while True:
        try:
            operand = int(input('>>> INGRESE UN NÚMERO NATURAL COMO DIVISOR:\n>>> '))
            if operand != 0:
                return operand
            else:
                print(msg)
        except:
            print(msg)

dividend = first_operand()
divisor = second_operand()

quotient = dividend // divisor
remainder = dividend % divisor

print(f'>>> COCIENTE: {quotient}\n>>> RESTO: {remainder}')
