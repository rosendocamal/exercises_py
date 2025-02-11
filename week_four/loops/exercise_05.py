# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

while True:
    try:
        initial_capital = float(input('>>> CAPITAL INICIAL:\n>>> $'))
        if initial_capital > 0:
            break
        else:
            print('>>> ERROR: INGRESE UN CAPITAL MAYOR QUE CERO')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO VÁLIDO COMO CAPITAL MAYOR QUE CERO')

while True:
    try:
        annual_interest = float(input('>>> INTERÉS ANUAL:\n>>> '))
        if annual_interest > 0:
            break
        else:
            print('>>> ERROR: INGRESE UN INTERÉS MAYOR QUE CERO')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO VÁLIDO COMO INTERÉS MAYOR QUE CERO')

while True:
    try:
        time = int(input('>>> NÚMERO DE AÑOS:\n>>> '))
        if time > 0:
            break
        else:
            print('>>> ERROR: INGRESE UN NÚMERO DE AÑOS MAYOR QUE CERO')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO VÁLIDO COMO PLAZO EN AÑOS MAYOR QUE CERO')

def interest(capital, interest, time):
    return round(capital * (1 + interest / 100) ** time, 2)

for i in range(1, time + 1, 1):
    print(f'>>> {i} AÑO DE INVERSIÓN: ${interest(initial_capital, annual_interest, i)}')
