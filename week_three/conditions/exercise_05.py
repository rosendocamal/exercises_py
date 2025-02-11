# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

while True:
    try:
        age = int(input('>>> INTRODUZCA SU EDAD:\n>>> '))
        if 0 < age < 130:
            break
        else:
            print('>>> ERROR: INTRODUZCA UNA EDAD VÁLIDA PARA CONTINUAR')
    except ValueError:
        print('>>> ERROR: INTRODUZCA UN NÚMERO ENTERO VÁLIDO COMO EDAD PARA CONTINUAR')

while True:
    try:
        income = float(input('>>> INTRODUZCA SU INGRESO MENSUAL:\n>>> '))
        break
    except ValueError:
        print('>>> ERROR: INTRODUZCA UN NÚMERO VÁLIDO COMO INGRESO MENSUAL')

if age > 16 and income >= 1000:
    print('>>> SUJETO DE IMPUESTO')
else:
    print('>>> NO SUJETO A IMPUESTO')
