# Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

def msg_error(var):
    return f'>>> INGRESE EL {var} VÁLIDO DEL PRODUCTO PARA CONTINUAR'

while True:
    product_name = input('>>> INTRODUZCA EL NOMBRE DEL PRODUCTO:\n>>> ')
    if bool(product_name):
        product_name = product_name.upper()
        break
    else:
        print(msg_error('NOMBRE'))

while True:
    product_price = input('>>> INTRODUZCA EL PRECIO UNITARIO DEL PRODUCTO:\n>>> ')
    try:
        if float(product_price) >= 0:
            break
        else:
            print(msg_error('PRECIO'))
    except:
        print(msg_error('PRECIO'))

while True:
    product_stock = input('>>> INTRODUZCA EL NÚMERO DE UNIDADES DEL PRODUCTO:\n>>> ')
    try:
        if int(product_stock) >= 0:
            break
        else:
             print(msg_error('NÚMERO DE UNIDADES'))   
    except:
        print(msg_error('NÚMERO DE UNIDADES'))

product_total_cost = float(product_price) * int(product_stock)

print(f'>>> PRODUCTO: {product_name}\n>>> PRECIO UNITARIO: ${float(product_price):09.2f}\n>>> EXISTENCIAS: {int(product_stock):03d}\n>>> COSTO TOTAL: ${float(product_total_cost):011.2f}')
