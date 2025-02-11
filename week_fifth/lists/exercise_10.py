# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

def min_and_max(numbers):
    return min(numbers), max(numbers)

def main():
    prices = [50, 75, 46, 22, 80, 65, 8]
    price_lower, price_higher = min_and_max(prices)
    
    print(f'>>> PRECIO MENOR: ${price_lower}\n>>> PRECIO MAYOR: ${price_higher}')

main()
