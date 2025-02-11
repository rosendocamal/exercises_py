# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

def read_input():
    while True:
        hours_worked = hours_cost = ''

        msg_error = '>>> INGRESE UNA CANTIDAD VÁLIDA DE'
        
        while True:
            hours_worked = input('>>> HORAS LABORADAS:\n>>> ')
            if bool(hours_worked):
                try:
                    float(hours_worked)
                    break
                except:
                    print(f'{msg} HORAS LABORADAS')
            else:
                print(f'{msg} HORAS LABORADAS')

        while True:
            hours_cost = input('>>> COSTE POR HORA:\n>>> ')
            if bool(hours_cost):
                try:
                    float(hours_cost)
                    break
                except:
                    print(f'{msg} COSTE POR HORA')
            else:
                print(f'{msg} COSTE POR HORA')

        return hours_cost, hours_worked

data_work = read_input()
print(data_work)
corresponding_pay = float(data_work[0]) * float(data_work[1])

print(f'>>> SALARIO CORRESPONDIDO: ${corresponding_pay}')
