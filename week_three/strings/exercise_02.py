# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

while True:
    msg = '>>> INTRODUZCA SU NOMBRE PARA CONTINUAR'
    try:
        name = input('>>> INGRESE SU NOMBRE:\n>>> ')
        if bool(name):
            break
        else:
            print(msg)
    except:
        print(msg)

print(f'>>> {name.lower()}')
print(f'>>> {name.upper()}')
print(f'>>> {name.title()}')
