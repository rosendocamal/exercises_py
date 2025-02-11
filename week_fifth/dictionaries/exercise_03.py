'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta 	Precio
Plátano 	1.35
Manzana 	0.80
Pera 	0.85
Naranja 	0.70
'''

fruits_kg_price = { 'plátano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70 }

def request_fruit(fruits):
    while True:
        fruit = input('>>> INGRESE LA FRUTA DESEADA:\n>>> ').strip().lower()
        if fruit in fruits:
            return fruit
        else:
            print(f'>>> ERROR: {fruit.upper()} NO SE ENCUENTRA EN EL REGISTRO, INTENTE CON OTRA FRUTA')
            
def request_kg():
    while True:
        try:
            kg = float(input('>>> INGRESE EL NÚMERO DE KILOGRAMOS:\n>>> '))
            if kg > 0:
                return kg
            else:
                print('>>> ERROR: INGRESE UN NÚMERO DE KG MAYOR QUE CERO')
        except ValueError:
            print('>>> ERROR: POR FAVOR, INGRESE UN NÚMERO VÁLIDO DE KG MAYOR QUE CERO')

def calculate_price(fruit, kg, fruits):
    return round(fruits[fruit] * kg, 2)

def show_price(fruit, kg, price):
    if price > 0:
        print(f'>>> EL PRECIO DE {kg} KG DE {fruit.upper()} ES ${price}')

def main():
    fruit = request_fruit(fruits_kg_price)
    kg = request_kg()
    price = calculate_price(fruit, kg, fruits_kg_price)
    show_price(fruit, kg, price)

if __name__ == '__main__':
    main()
