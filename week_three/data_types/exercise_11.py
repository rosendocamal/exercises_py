'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.
'''

while True:
    try:
        initial_capital = float(input('>>> AHORRO INICIAL:\n>>> '))
        if initial_capital >= 0:
            break
        else:
            print('>>> INGRESA UN VALOR MAYOR 0')
    except:
        print('>>> INGRESA UNA CANTIDAD VÁLIDA PARA CONTINUAR')

annual_interest = 4

for i in range(3):
    print(f'>>> AÑO {i + 1}: {round(initial_capital * (1 + (annual_interest / 100)) ** (i + 1), 2)}')
