import math
from decimal import Decimal

decimal = input('INGRESE UN NÚMERO DECIMAL:\n\b')

def convertir_fraccion_comun(decimal):
    ''' 
    Para convertir un número decimal a fracción común se utiliza la siguiente formúla:
        (R - v) / (10^h - 10^c)
    Donde:
        R: es el entero que resulta de recorrer el punto decimal hasta la última cifra del periodo.
        h: lugares recorridos para obtener R.
        v: es el entero que resulta de recorrer el punto hasta una cifra antes del periodo.
        c: lugares reorridos para obtener v.
    '''    
    # PRIMERA FASE: NÚMEROS DECIMALES NO PERIÓDICOS
    def no_periodicos(decimal):
        h = denominador = 10 ** ((len(decimal)) - (decimal.find('.') + 1))
        R = numerador = int(float(decimal) * h) 
        return ('{}/{}'.format(numerador, denominador))

    # SEGUNDA FASE: NÚMEROS DECIMALES PERIÓDICOS
    def si_periodicos(decimal):
        numero_digitos_periodicos = (decimal.find(')') - decimal.find('(')) - 1
    
        decimal_digitos = list()
        for i in range(0, len(decimal), 1):
            if decimal[i] != '(' and decimal[i] != ')':
                decimal_digitos.append(decimal[i])
    
        parte_periodica = ''.join(decimal_digitos)[-1 * numero_digitos_periodicos:]
        decimal_digitos.extend(parte_periodica * 2)
        x = denominador = Decimal(''.join(decimal_digitos))
        decimal_digitos.extend(parte_periodica)
        y = numerador = Decimal(''.join(decimal_digitos)) * 10 ** numero_digitos_periodicos - x

        contador = numero_digitos_periodicos
        while int(y) != float(y):
            y *= 10
            contador += 1

        numerador = int(y)
        denominador = ((10 ** numero_digitos_periodicos) - (1 ** numero_digitos_periodicos)) * 10 ** (abs(contador - numero_digitos_periodicos)) # type: ignore
        return ('{}/{}'.format(numerador, denominador))

    # ELECCIÓN ENTRE FUNCIONES PARA NÚMEROS DECIMALES PERIÓDICOS Y NO PERIÓDICOS

    if decimal.find('(') != -1 and decimal.find(')'):
        print(si_periodicos(decimal))
    else:
        print(no_periodicos(decimal))

convertir_fraccion_comun(decimal)




