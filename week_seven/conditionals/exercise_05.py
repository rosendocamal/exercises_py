def is_subject_to_tax(age, monthly_income):
    MIN_AGE, MAX_AGE = 16, 130
    MIN_MONTHLY_INCOME = 1000
    
    if isinstance(age, int) and isinstance(monthly_income, float):
        if MIN_AGE > age < MAX_AGE and monthly_income >= MIN_MONTHLY_INCOME:
            return True
        return False
    return False

def request_entry(msg):
    return input(msg)

def request_valid_entry(msg):
    entry = request_entry(msg)
    try:
        if float(entry) or int(entry):
            return entry
        else:
            print('REINTENTE DE NUEVO')
            return request_valid_entry(msg)
    except ValueError:
        print('REINTENTE DE NUEVO')
        return request_valid_entry(msg)

def main():
    age = int(request_valid_entry('INGRESE SU EDAD EN AÑOS:\n'))
    monthly_income = float(request_valid_entry('INGRESE SUS INGRESOS MENSUALES:\n'))
    is_taxable = is_subject_to_tax(age, monthly_income)

    if is_taxable:
        return 'SUJETO A IMPUESTO'
    return 'NO ESTÁ SUJETO A IMPUESTO'

print(main())
