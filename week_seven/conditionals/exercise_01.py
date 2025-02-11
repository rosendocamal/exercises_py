def get_age():
    try:
        age = int(input('INGRESE SU EDAD:\n'))
        if 0 <= age < 130:
            return age
        #return False
        #NO ENTIENDO POR QUÉ ESTA LÍNEA IMPIDE QUE SE EJECUTE CORRECTAMENTE EL CÓDIGO
        #MEDIA HORA POR MI CUENTA
        #15 MIN CON CHATGPT
        #DEBERÍA PUBLICARLO EN STACKOVERFLOW
    except ValueError:
        return False

def show_msg(msg):
    print(msg)

while True:
    age = get_age()
    #print(f'VALOR DE "{age}": {type(age)}')
    if isinstance(age, int):
        break

show_msg('ES MAYOR DE EDAD' if age >= 18 else 'ES MENOR DE EDAD')
