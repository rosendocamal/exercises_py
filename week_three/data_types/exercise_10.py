# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
# Cada payaso pesa 112 g y cada muñeca 75 g.
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

weight_gram_clown = 112
weight_gram_doll = 75

while True:
    try:
        sale_doll = int(input('>>> ÚLTIMAS PIEZAS VENDIDAS (MUÑECAS):\n>>> '))
        break
    except:
        print('>>> INGRESE UNA CANTIDAD VÁLIDA')

while True:
    try:
        sale_clown = int(input('>>> ÚLTIMAS PIEZAS VENDIDAS (PAYASOS):\n>>> '))
        break
    except:
        print('>>> INGRESE UNA CANTIDAD VÁLIDA')

package_weight = (sale_doll * weight_gram_doll) + (sale_clown * weight_gram_clown)

print(f'>>> PESO DEL PAQUETE: {round(package_weight / 1000, 2)} KG')
