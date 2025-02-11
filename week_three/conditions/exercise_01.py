# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

while True:
    try:
        age = int(input('>>> INGRESE SU EDAD:\n>>> '))
        if age >= 0:
            break
        else:
            print('>>> INGRESE UNA EDAD VÁLIDA')
    except:
        print('>>> INGRESE UNA EDAD VÁLIDA')

if age >= 18:
    print('>>> ES MAYOR DE EDAD')
else:
    print('>>> ES MENOR DE EDAD')
