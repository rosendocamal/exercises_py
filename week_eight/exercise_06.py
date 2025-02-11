def return_group(name, sex):
    if sex == 'M':
        if name[0] > 'N':
            return 'A'
        return 'B'
    if sex == 'F':
        if name[0] < 'M':
            return 'A'
        return 'B'

while True:
    name_student = input('INGRESE SU NOMBRE:\n').strip().lower()
    if name_student.isalpha():
        break

while True:
    sex_student = input('INGRESE SU SEXO (M/F):\n').strip().upper()
    if sex_student.isalpha():
        if sex_student == 'M' or sex_student == 'F':
            break

group = return_group(name_student, sex_student)

print(f'LE CORRESPONDE EL GRUPO "{group}"')
