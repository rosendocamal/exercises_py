'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    Preguntar por el NIF del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    Terminar el programa.
'''

customers = {
        'ADMINISTRATOR_ROOT':{
            'name': 'root',
            'address': 'root',
            'phone': '0000000000',
            'mail': 'root@root.root',
            'preferential': 'TRUE'
            },
        'ADMINISTRATOR_TEST':{
            'name': 'test',          
            'address': 'test',       
            'phone': '0000000000',   
            'mail': 'test@test.test',
            'preferential': 'TRUE'
            }
        }

def add_customer():
    while True:
        print('>>> INGRESE LOS DATOS DEL CLIENTE:')
        while True:
            nif = input('>>> INGRESE EL NIF DEL CLIENTE:\n>>> ').strip().upper()
            if nif:
                customers.update({nif: {}})
                break
            else:
                print('>>> ERROR: POR FAVOR, INGRESE EL NIF DEL CLIENTE')
        
        while True:
            name = input('>>> 1. NOMBRE:\n>>> ').strip().upper()
            if name:
                customers[nif].update({'name': name})
                break
            else:
                print('>>> ERROR: POR FAVOR, INGRESE EL NOMBRE DEL CLIENTE')

        while True:
            address = input('>>> 2. DOMICILIO:\n>>> ').strip().upper()
            if address:
                customers[nif].update({'address': address})
                break
            else:
                print('>>> ERROR: POR FAVOR, INGRESE EL DOMICILIO DEL CLIENTE')

        while True:
            phone = input('>>> 3. TELÉFONO:\n>>> ').strip().upper()
            if len(phone) == 10 and phone.isdigit():
                customers[nif].update({'phone': phone})
                break
            else:
                print('>>> ERROR: POR FAVOR, INGRESE EL TELÉFONO DEL CLIENTE')
                
        while True:
            mail = input('>>> 4. CORREO:\n>>> ').strip().upper()
            if bool(mail) and len(mail) >= 5 and mail.rfind('@', 1) >= 1 and mail.count('@') == 1:
                    customers[nif].update({'mail': mail})
                    break
            else:
                print('>>> ERROR: POR FAVOR, INGRESE EL CORREO DEL CLIENTE')

        while True:
            preferential = input('>>> 5. CLIENTE PREFERENCIAL:\n>>> ').strip().upper()
            if preferential == 'TRUE' or preferential == 'FALSE':
                customers[nif].update({'preferential': preferential})
                break
            else:
                print('>>> ERROR: POR FAVOR, INGRESE "TRUE" SI ES CLIENTE PREFERENCIAL, DE LO CONTRARIO, INGRESE "FALSE"')
        print('>>> EL CLIENTE HA SIDO REGISTRADO CON ÉXITO')
        break
        
def delete_customer():
    while True:
        nif = input('>>> PARA ELIMINAR AL CLIENTE DEL REGISTRO, INGRESE SU NIF:\n>>> ').strip().upper()
        if nif in customers:
            customers.pop(nif)
            print('>>> EL CLIENTE HA SIDO ELIMINADO CON ÉXITO')
            break
        else:
            print('>>> ERROR: NO SE ENCUENTRA EL USUARIO REGISTRADO. INTENTE DE NUEVO')


def show_customer():
    while True:
        nif = input('>>> PARA MOSTRAR LA INFORMACIÓN DEL CLIENTE, INGRESE SU NIF:\n>>> ').strip().upper()
        if nif in customers:
            print('>>>')
            for key in customers[nif].keys():
                print(f'>>>>>> {key.upper()}: {customers[nif][key]}')
            print('>>>')
            break
        else:
            print('>>> ERROR: NO SE ENCUENTRA EL USUARIO REGISTRADO. INTENTE DE NUEVO')

def list_all_customer():
    print('>>>')
    print('>>> CLIENTES REGISTRADOS')
    for nif in customers.keys():
        print(f'>>>>>> {nif}, {customers[nif]["name"]}')
    print('>>>')

def list_preferred_customer():
    print('>>>')
    print('>>> CLIENTES PREFERENTES REGISTRADOS')
    for nif in customers.keys():
        if customers[nif]['preferential'] == 'TRUE':
            print(f'>>>>>> {nif}, {customers[nif]["name"]}')
    print('>>>')

def run_menu_option(option):
    if option == 1:
        add_customer()
    elif option == 2:
        delete_customer()
    elif option == 3:
        show_customer()
    elif option == 4:
        list_all_customer()
    elif option == 5:
        list_preferred_customer()

def get_menu_option():
    while True:
        try:
            option = int(input('>>> '))
            if 1 <= option <= 6:
                return option
            else:
                print('>>> ERROR: INGRESE UNA OPCIÓN ENTRE 1 Y 6')
        except ValueError:
            print('>>> ERROR: INGRESE UNA OPCIÓN VÁLIDAD ENTRE 1 Y 6')
def show_menu():
    while True:
        print('>>> REGISTRO DE CLIENTES. INGRESE UNA OPCIÓN:')
        print('>>> (1) AÑADIR CLIENTE')
        print('>>> (2) ELIMINAR CLIENTE')
        print('>>> (3) MOSTRAR CLIENTE')
        print('>>> (4) LISTAR TODOS LOS CLIENTES')
        print('>>> (5) LISTAR CLIENTES PREFERENTES')
        print('>>> (6) TERMINAR')

        option = get_menu_option()
        if option == 6:
            break
        run_menu_option(option)

def main():
    show_menu()

if __name__ == '__main__':
    main()
