'''
Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
'''


fresh_bread = 3.49
discount = 0.6

while True:
    non_fresh_bread_sale = input('>>> VENTA DE PIEZAS DE PAN NO FRESCOS:\n>>> ')
    try:
        if non_fresh_bread_sale != '':
            if int(non_fresh_bread_sale):
                break
            else:
                print('>>> INGRESE UNA CANTIDAD VÁLIDA')
    except:
        print('>>> INGRESE UNA CANTIDAD VÁLIDA')

usual_price = round(fresh_bread * int(non_fresh_bread_sale), 2)
total_discount = round(usual_price * discount, 2)
final_cost = round(usual_price - total_discount, 2)
print(f'>>>\n>>> PRECIO HABITUAL: ${usual_price}\n>>> DESCUENTO: ${total_discount}\n>>> COSTE FINAL: ${final_cost}')
