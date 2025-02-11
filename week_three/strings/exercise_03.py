# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

while True:
    msg = '>>> INGRESE SU NOMBRE PARA CONTINUAR'
    try:
        name = input('>>> INGRESE SU NOMBRE:\n>>> ')
        if bool(name):
            break
        else:
            print(msg)
    except:
        print(msg)

lyrics_num = 0
for i in name:
    if i.isalpha():
        lyrics_num += 1

print(f'>>> {name.upper()} TIENE {lyrics_num} LETRAS')
