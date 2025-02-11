# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

while True:
    try:
        user_age = int(input('>>> INGRESE SU EDAD:\n>>> '))
        if 1 <= user_age <= 130:
            print('>>>')
            for age in range(user_age):
                print(f'>>> {age + 1:3d}')         
            break
        else:
            print('>>> ERROR: INGRESE UNA EDAD VÁLIDA ENTRE 1 Y 130')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO ENTERO VÁLIDO COMO EDAD')


