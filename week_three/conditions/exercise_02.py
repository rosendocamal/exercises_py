# Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = 'contraseña'

attemps = 3
while attemps > 0:
    user_password = input('>>> INGRESE LA CONTRASEÑA:\n>>> ')
    if bool(user_password) and user_password.lower() == password.lower():
        print('>>> CONTRASEÑA CORRECTA')
        break
    else:
        attemps -= 1
        if attemps > 0:
            print(f'>>> CONTRASEÑA INCORRECTA. TE QUEDAN {attemps} INTENTO(S)')
        else:
            print(f'>>> HAZ AGOTADO TODOS LOS INTENTOS. PROGRAMA FINALIZADO')
