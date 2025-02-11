# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

import getpass

while True:
    stored_password = getpass.getpass('>>> CREA UNA CONTRASEÑA:\n>>> ')
    if stored_password != '' and stored_password == getpass.getpass('>>> REPITA LA CONTRASEÑA:\n>>> '):
        print('>>> CONTRASEÑA ESTABLECIDA CORRECTAMENTE')
        break
    elif stored_password == '':
        print('>>> CONTRASEÑA VACÍA. INGRESE UNA CONTRASEÑA PARA CONTINUAR')
    else:
        print('>>> LAS CONTRASEÑAS NO COINCIDEN. INTENTE DE NUEVO')

print('>>>')

while True:
    user_input_pswd = getpass.getpass('>>> INTRODUZCA SU CONTRASEÑA:\n>>> ')
    if user_input_pswd == stored_password:
        print('>>> CONTRASEÑA CORRECTA. ACCESO PERMITIDO')
        break
    elif user_input_pswd == '':
        print('>>> INGRESE UNA CONTRASEÑA')
    else:
        print('>>> CONTRASEÑA INCORRECTA. INTENTE DE NUEVO')

# ADVERTENCIA: CONTRASEÑAS EN TEXTO PLANO. SE RECOMIENDA EL USO DE BCRYPT, Y SI SE DESEA ALGO BÁSICO EL USO DE HASHLIB
