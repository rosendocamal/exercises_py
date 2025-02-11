'''
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
Lista de la compra 	
Artículo 1 	Precio
Artículo 2 	Precio
Artículo 3 	Precio
… 	…
Total 	Coste

'''
products_and_price = dict()

finish = False
while finish != True:
    while True:
        product = input('>>> INGRESE EL NOMBRE DEL PRODUCTO:\n>>> ').strip().upper()
        if product:
            break
        else:
            print('>>> ERROR: POR FAVOR, INGRESE EL NOMBRE DEL PRODUCTO')

    while True:
        try:
            price = float(input('>>> INGRESE EL PRECIO DEL PRODUCTO:\n>>> $'))
            if price >= 0:
                break
            else:
                print('>>> ERROR: INGRESE UN PRECIO VÁLIDO IGUAL O MAYOR QUE 0')
        except ValueError:
            print('>>> ERROR: POR FAVOR, INGRESE UN PRECIO VÁLIDO PARA CONTINUAR')

    products_and_price.update({product: price})

    while True:
        answer = input('>>> ¿DESEA AÑADIR MÁS PRODUCTOS A LA CANASTA?\n>>> (SÍ) O (NO):  ').strip().upper()
        if answer != '':
            if answer == 'SÍ':
                finish = False
                break
            elif answer == 'NO':
                finish = True
                break
            else:
                print('>>> ERROR: OPCIÓN NO VÁLIDA, INGRESE "SÍ" O "NO"')
        else:
            print('>>> ERROR: POR FAVOR, INGRESE UNA OPCIÓN VÁLIDA')

total_cost = 0
print('>>> LISTA DE COMPRA')
for product in products_and_price.keys():
    print(f'>>> {product[:10]:<10}\t${products_and_price[product]: 8.2f}')
    total_cost += products_and_price[product]
print(f'>>> TOTAL: ${total_cost}')
