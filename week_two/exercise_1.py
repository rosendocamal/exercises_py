'''
Ejercicio 1: Calculadora de Edad en Días

Descripción:

El usuario ingresará su fecha de nacimiento (en formato DD-MM-AAAA), y el programa debe calcular cuántos días han pasado desde esa fecha hasta la fecha actual. El programa debe manejar bien los años bisiestos, así que deberá tener en cuenta esos detalles.

Requerimientos:

Solicitar la fecha de nacimiento del usuario (como string).
Utilizar tipos de datos como int, str, y date para manipular fechas.
Calcular la diferencia de días usando el módulo datetime.
Mostrar el resultado en un formato adecuado.
'''
import re
import datetime

def read_input():
    # Validar el valor de la fecha con el formato adecuado y dicha fecha sea válida
    while True:
        user_birth_date = input('>>> FECHA DE NACIMIENTO:\n>>> FORMATO DD-MM-AAAA\n>>> ')
        
        regex = '([0-2][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/]([0-9]{4})'
        if re.fullmatch(regex, user_birth_date):
            try:
                datetime.date(int(user_birth_date[6:]), int(user_birth_date[3:5]), int(user_birth_date[:2]))
                return user_birth_date
            except ValueError:
                print('>>> LA FECHA NO ES VÁLIDA')
        else:
            print('>>> LA FECHA NO TIENE EL FORMATO CORRECTO')

def is_leap_year(year):
    # Validar que el año ingresado sea bisiesto o no
    value = False
    if year % 4 == 0:
        if year % 100 or year % 400:
            value = True
    return value

def current_now():
    # Fecha de hoy
    return f'{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}'


# Realizar una suma de los días desde la fecha de nacimiento hasta el día de hoy

days_month = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_passed = 0

birth_date = read_input()
date_now = current_now()

for year in range(int(birth_date[6:]) + 1, int(date_now[6:]), 1):
    if is_leap_year(year):
        days_passed += 366
    else:
        days_passed += 365

for month in range(int(birth_date[3:5]), len(days_month), 1):
    if month == 1:
        if is_leap_year(int(birth_date[6:])):
            days_passed += days_month[month][1]
        else:
            days_passed += days_month[month][0]
    else:
        days_passed += days_month[month]

for month in range(0, int(date_now[3:5]) - 1, 1):
    if month == 1:
        if is_leap_year(int(date_now[6:])):
            days_passed += days_month[month][1]
        else:
            days_passed += days_month[month][0]
    else:
        days_passed += days_month[month]

if is_leap_year(int(birth_date[6:])):
    if int(birth_date[3:5]) - 1 == 1:
        days_passed += days_month[int(birth_date[3:5] - 1)][1] - int(birth_date[:2])
    else:
        days_passed += days_month[int(birth_date[3:5]) - 1] - int(birth_date[:2])
else:
    if int(birth_date[3:5]) - 1 == 1:
        days_passed += days_month[int(birth_date[3:5]) - 1][0] - int(birth_date[:2])
    else:
        days_passed += days_month[int(birth_date[3:5]) - 1] - int(birth_date[:2])

if is_leap_year(int(date_now[6:])):
    if int(date_now[3:5]) - 1 == 1:
        days_passed += int(date_now[:2])
    else:
        days_passed += int(date_now[:2])
else:
    if int(date_now[3:5]) - 1 == 1:
        days_passed += int(date_now[:2])
    else:
        days_passed += int(date_now[:2])

print(days_passed)
