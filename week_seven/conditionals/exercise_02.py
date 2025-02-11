password = 'contrasena'

attempts = 3
while attempts > 0:
    password_entered = input('INGRESE LA CONTRASEÑA:\n')
    if password_entered.upper() == password.upper():
        print('CONTRASEÑA CORRECTA\nACCESO PERMITIDO')
        break
    else:
        attempts -= 1
        print('CONTRASEÑA INCORRECTA. ACCESO DENEGADO')
        print(f'QUEDAN {attempts} INTENTO(S)')
