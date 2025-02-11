# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def validate_date(day, month, year):
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            return True
        return False

    days = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1<= month <= 12 and 1 <= day <= days[month - 1]:
        return True
    return False


while True:
    birth_date = input('>>> INTRODUZCA TU FECHA DE NACIMIENTO (DD/MM/AAAA):\n>>> ')
    try:

            birth_day = int(birth_date[:2])
            birth_month = int(birth_date[3:5])
            birth_year = int(birth_date[6:])

            if bool(birth_date) and len(birth_date) == 10 and validate_date(birth_day, birth_month, birth_year):
                break
    except:
        print('>>> INGRESE UNA FECHA VÁLIDA')

print(f'>>> DÍA: {birth_day}\n>>> MES: {birth_month}\n>>> AÑO: {birth_year}')
