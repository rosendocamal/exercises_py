'''
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta: 	Tipo impositivo
Menos de 10000€: 	5%
Entre 10000€ y 20000€: 	15%
Entre 20000€ y 35000€: 	20%
Entre 35000€ y 60000€: 	30%
Más de 60000€: 	45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''

def get_annual_income():
    while True:
        try:
            income = float(input('>>> INTRODUZCA SUS INGRESOS ANUALES:\n>>> '))
            return income
        except ValueError:
            print('>>> INGRESE UN NÚMERO VÁLIDO COMO INGRESO ANUAL')

def get_tax_rate(annual_income):
    if annual_income <= 0:
        return 'INGRESOS NO SUJETO A IMPUESTO'
    elif annual_income <= 10000:
        return 5
    elif annual_income <= 20000:
        return 15
    elif annual_income <= 35000:
        return 20
    elif annual_income <= 60000:
        return 30
    else:
        return 45


annual_income = get_annual_income()
tax_rate = get_tax_rate(annual_income)
if isinstance (tax_rate, str):
    print(f'>>> {tax_rate}')
else:
    print(f'>>> TASA IMPOSITIVA DEL {tax_rate}%')
