# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def get_data_user(dictionary):
    if isinstance(dictionary, dict): 
        while True:
            user_name = input('>>> INGRESE SU NOMBRE:\n>>> ').strip()
            if user_name:
                dictionary.update({'name': user_name})
                break
            else:
                print('>>> ERROR: POR FAVOR, INGRESE SU NOMBRE PARA CONTINUAR')

        while True:
            MIN_AGE = 1
            MAX_AGE = 120
            try:
                user_age = int(input('>>> INGRESE SU EDAD:\n>>> '))
                if MIN_AGE <= user_age <= MAX_AGE:
                    dictionary.update({'age': user_age})
                    break
                else:
                    print(f'>>> ERROR: INGRESE UNA EDAD ENTRE {MIN_AGE} Y {MAX_AGE}')
            except ValueError:
                print('>>> ERROR: INGRESE UN NÚMERO ENTERO VÁLIDO PARA CONTINUAR')

        while True:
            user_address = {
                    'street': '',
                    'inside_number': '',
                    'outer_number': '',
                    'colony': '',
                    'city': '',
                    'country': '',
                    }
            print('>>> INGRESE SU DIRECCIÓN:\n>>> ')
            for data in user_address.keys():
                print(data)
                if data == 'street':
                    user_address[data] = input('>>> CALLE Y AVENIDA: ')
                if data == 'inside_number':
                    user_address[data] = input('>>> NÚMERO INTERIOR: ')
                if data == 'outer_number':
                    user_address[data] = input('>>> NÚMERO EXTERIOR: ')
                if data == 'colony':
                    user_address[data] = input('>>> COLONIA: ')
                if data == 'city':
                    user_address[data] = input('>>> CIUDAD: ')
                if data == 'country': 
                    user_address[data] = input('>>> PAÍS: ')
            dictionary.update({'address': user_address})
            break

        while True:
            try:
                user_phone = int(input('>>> INGRESE SU NÚMERO TELEFÓNICO:\n>>> '))
                if len(str(user_phone)) == 10:
                    dictionary.update({'phone': user_phone})
                    break
                else:
                    print('>>> ERROR: INGRESE UN NÚMERO TELEFÓNICO CON UNA LONGITUD DE 10 NÚMEROS') 
            except ValueError:
                print('>>> ERROR: INGRESE UN NÚMERO TELEFÓNICO VÁLIDO PARA CONTINUAR')

        
    return dictionary

def main():
    data_user = get_data_user({})
    print(f'>>> {data_user.get("name")} TIENE {data_user.get("age")} AÑOS, VIVE EN {data_user.get("address").get("city")} Y SU NÚMERO DE TÉLEFONO ES {data_user.get("phone")}')

main()
