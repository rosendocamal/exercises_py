# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

def input_weight():
    msg = '>>> PESO INVÁLIDO'
    while True:
        try:
            weight = float(input('>>> INGRESA TU PESO (KG):\n>>> '))
            if weight > 0:
                return weight
            else:
                print(msg)
        except:
            print(msg)

def input_height():
    msg = '>>> ESTATURA INVÁLIDA'
    while True:
        try:
            height = float(input('>>> INGRESA TU ESTATURA (M):\n>>> '))
            if height > 0:
                return height
            else:
                print(msg)
        except:
            print(msg) 

user_weight = input_weight()
user_height = input_height()

imc = user_weight / (user_height ** 2)

print(f'>>> TU ÍNDICE DE MASA CORPORAL ES {round(imc, 2)}')
