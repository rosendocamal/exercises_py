def get_annual_income():
    while True:
        try:
            annual_income = float(input('INTRODUZCA SU INGRESO ANUAL:\n$'))
            if annual_income >= 0:
                return annual_income
            else:
                print('LOS INGRESOS DEBEN SER MAYORES A CERO')
        except ValueError:
            print('REINTENTE DE NUEVO')

def apply_tax(annual_income):
    FIRST_LEVEL_INCOME = 10000
    SECOND_LEVEL_INCOME = 20000
    THIRD_LEVEL_INCOME = 35000
    FOURTH_LEVEL_INCOME = 60000

    if annual_income < FIRST_LEVEL_INCOME:
        return 0.05
    elif FIRST_LEVEL_INCOME <= annual_income < SECOND_LEVEL_INCOME:
        return 0.15
    elif SECOND_LEVEL_INCOME <= annual_income < THIRD_LEVEL_INCOME:
        return 0.2
    elif THIRD_LEVEL_INCOME <= annual_income < FOURTH_LEVEL_INCOME:
        return 0.3
    elif annual_income >= FOURTH_LEVEL_INCOME:
        return 0.45

annual_income = get_annual_income()
tax_rate = apply_tax(annual_income)

print(f'TASA DE IMPUESTO CORRESPONDIENTE AL {tax_rate * 100}%')
