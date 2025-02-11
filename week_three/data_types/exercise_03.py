# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

while True:
    user_name = input('>>> ¿CUÁL ES SU NOMBRE?:\n>>> ')
    if bool(user_name):
        break
    else:
        print('>>> INGRESE ALGÚN NOMBRE PARA CONTINUAR')

msg = f'¡HOLA {user_name.upper()}!'

print(f'>>> {msg}')
