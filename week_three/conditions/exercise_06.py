# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def get_name():
    while True:
        name = input('>>> INGRESE SU PRIMER NOMBRE:\n>>> ')
        if bool(name):
            return name.strip().lower()[0]
        else:
            print('>>> INGRESE UN NOMBRE VÁLIDO')

def get_sex():
    while True:
        sex = input('>>> INGRESE SU SEXO:\n>>> ')
        if bool(sex):
            sex = sex.strip().lower()
            if sex == 'femenino' or sex == 'mujer' or sex == 'f':
                return 'MUJER'
            elif sex == 'masculino' or sex == 'hombre' or sex == 'm':
                return 'HOMBRE'
            else:
                print('>>> INGRESE UN SEXO VÁLIDO')
        else:
            print('>>> INGRESE UN SEXO VÁLIDO')

def get_group(name, sex):
    characters = 'aábcdeéfghiíjklmnñoópqrstuúüvwxyz'
    student_name = name
    student_sex = sex
    student_group = 'NO ESTÁ DEFINIDO'

    if student_sex == 'MUJER':
        if student_name in characters[:15]:
            student_group = 'A'
        else:
            student_group = 'B'
    if student_sex == 'HOMBRE':
        if student_name in characters[16:]:
            student_group = 'A'
        else:
            student_group = 'B'
    return student_group

name = get_name()
sex = get_sex()
group = get_group(name, sex)
print(f'>>> GRUPO {group}')
