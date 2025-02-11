# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

while True:
    msg = '>>> INTRODUZCA UN NÚMERO CON EL FORMATO +34-XXXXXXXXX-XX'
    try:
        tel = input('>>> INGRESE EL NÚMERO DE TELÉFONO:\n>>> ')
        if bool(tel):
            if tel[0:4] == '+34-' and tel[-3:-2] == '-' and len(tel) == 16:
                break
            else:
                print(msg)
        else:
            print(msg)
    except:
        print(msg)

print(f'>>> {tel[4:-3]}')
