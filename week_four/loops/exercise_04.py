# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

while True:
    try:
        number = int(input('>>> INGRESE UN NÚMERO NATURAL:\n>>> '))
        if number >= 1:
            descendant_series = []
            for i in range(number, - 1, - 1):
                descendant_series.append(str(i))
            print(f'>>> {", ".join(descendant_series)}')
            break
        else:
            print('>>> ERROR: INGRESE UN NÚMERO ENTERO MAYOR QUE CERO')
    except:
        print('>>> ERRROR. INGRESE UN NÚMERO ENTERO VÁLIDO MAYOR QUE CERO')
