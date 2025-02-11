# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

user_personal_information = dict()

continue_adding = True
while continue_adding:
    data_type = input('>>> TIPO DE INFORMACIÓN A INGRESAR:\n>>> ')
    user_data = input('>>> INGRESE SU INFORMACIÓN CORRESPODIENTE:\n>>> ')
    user_personal_information.update({data_type: user_data})

    print(f'>>> {user_personal_information}') 
   
    while True:
        ask = input('>>> DESEA AÑADIR MÁS INFORMACIÓN ("SÍ" O "NO"):\n>>> ').strip().upper()
        if ask == 'SÍ' or ask == 'NO':
            if ask == 'SÍ':
                continue_adding = True
                break
            if ask == 'NO':
                continue_adding = False
                break
        else:
            print('>>> ERROR: OPCIÓN INVÁLIDA. INGRESE "SÍ" O "NO"')
