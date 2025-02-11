# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

days_per_month = {
        'enero': 31,
        'febrero': 28,
        'marzo': 31,
        'abril': 30,
        'mayo': 31,
        'junio': 30,
        'julio': 31,
        'agosto': 31,
        'septiembre': 30,
        'octubre': 31,
        'noviembre': 30,
        'diciembre': 31
        }

def get_date():
    while True:
        date = input('>>> INGRESE LA FECHA CON FORMATO DD/MM/AAAA:\n>>> ')
        try:
            if len(date) == 10:
                dd, mm, yyyy = date[:2], date[3:5], date[6:]
                
                if len(dd) == 2 and len(mm) == 2 and len(yyyy) == 4:
                    return int(dd), int(mm), int(yyyy)
        except ValueError:
            print('>>> ERROR: POR FAVOR, INGRESE LA FECHA (DD/MM/AAAA) CON NÚMEROS ENTEROS')

def is_leap_year(yyyy):
    if yyyy % 4 == 0:
        if yyyy % 100 == 0:
            if yyyy % 400 == 0:
                return True
            return False
        return True
    return False

def is_correct_date(dd, mm, yyyy):
    names_month = list(days_per_month.keys())
    value = names_month[mm - 1]

    if value == 'febrero':
        if is_leap_year(yyyy):
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        days_in_month = days_per_month[value]

    if 1 <= dd <= days_in_month:
        return True
    return False

def return_valid_date():
    while True:
        dd, mm, yyyy = get_date()
        if is_correct_date(dd, mm, yyyy):
            return dd, mm, yyyy
        else:
            print('>>> ERROR: POR FAVOR, INGRESE UNA FECHA VÁLIDA')

def show_formatted_date(dd, mm, yyyy):
    names_month = list(days_per_month.keys())
    name_month = names_month[mm - 1]
    print(f'>>> {dd} DE {name_month.upper()} DE {yyyy}') 

def main():
    day, month, year = return_valid_date()
    show_formatted_date(day, month, year)

if __name__ == '__main__':
    main()
