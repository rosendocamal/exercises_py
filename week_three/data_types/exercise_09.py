# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

def data():
    msg_min = '>>> INTRODUZCA UN VALOR MAYOR A 0 PARA CONTINUAR'
    msg_error = '>>> INTRODUZCA UNA CANTIDAD VÁLIDAD PARA CONTINUAR'

    while True:

        while True:
            try:
                initial_capital = float(input('>>> CAPITAL INICIAL:\n>>> '))
                if initial_capital > 0:
                    break
                else:
                    print(msg_min)
            except:
                print(msg_error)

        while True:
            try:
                annual_interest = float(input('>>> INTERES ANUAL:\n>>> '))
                if annual_interest > 0:
                    break
                else:
                    print(msg_min)
            except:
                print(msg_error)

        while True:
            try:
                investment_time = float(input('>>> PLAZO EN AÑOS:\n>>> '))
                if investment_time > 0:
                    break
                else:
                    print(msg_min)
            except:
                print(msg_error)

        return initial_capital, annual_interest, investment_time

initial_capital, annual_interest, investment_time = data()

final_capital = initial_capital * (1 + (annual_interest / 100)) ** investment_time

print(f'>>> CAPITAL FINAL: {round(final_capital, 2)}')
