# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

while True:
    msg = '>>> INTRODUZCA SU NOMBRE PARA CONTINUAR'
    try:
        user_name = input('>>> INGRESE SU NOMBRE:\n>>> ')
        if bool(user_name):
            break
        else:
            print(msg)
    except:
        print(msg)

while True:
    try:
        user_num = int(input('>>> INGRESE UN NÚMERO:\n>>> '))
        if user_num > 0: 
            break
        else:
            print('>>> INTRODUZCA UN NÚMERO MAYOR A CERO')
    except:
        print('>>> INTRODUZCA ALGÚN NÚMERO PARA CONTINUAR')


print(f'>>> {user_name}\n' * user_num) 
