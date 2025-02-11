# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

while True:
    shopping_products = input('>>> INGRESE LOS PRODUCTOS COMPRADOS SEPARADOS CON COMA:\n>>> ')
    if shopping_products:
        products = [product.strip() for product in shopping_products.split(',')]
        break
    else:
        print('>>> INGRESE UNA LISTA VÁLIDA CON EL FORMATO ADECUADO')

for product in products:
    print(f'>>> {product.upper()}')
