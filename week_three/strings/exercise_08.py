# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

while True:
    price = input('>>> INGRESE EL PRECIO DEL PRODUCTO:\n>>> ')
    try:
        if bool(price) and float(price) >= 0 and len(price[price.index('.') + 1:]) >= 1:
            break
    except:
        print('>>> INTRODUZCA UN PRECIO VÁLIDO')

print(f'>>> {price[:price.index(".")]} EURO(S) Y {price[price.index(".") + 1:]} CÉNTIMO(S)')
