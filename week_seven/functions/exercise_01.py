# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

def get_discount(price, percentage):
    '''
    Función que aplica un descuento
    Parámetros:
        price: Es el precio original al cual se le aplica el descuento
        percentage: Es el porcetanje del descuento a aplicar
    Devuelve:
        El precio final tras aplicar el descuento
    '''
    return price - price * (percentage / 100)

def get_tax(price, percentage):
    '''
    Función que aplica el impuesto
    Parámetros:
        price: Es el precio original al cual se le aplica el impuesto
        percentage: Es el porcetanje del impuesto por aplicar
    Devuelve:
        El precio final con impuesto incluido
    '''
    return price + price * (percentage / 100)

def return_prices(prices_percentages, function):
    '''
    Función que aplica a los precios los porcentajes indicandos de acuerdo a la función elegida
    Parámetros:
        prices_percentages: Es un diccionario formado por el par price:percentage
        function: Es una función que toma dos valores y devuelve otro. Normalmente aplicar el impuesto o un descuento
    Devuelve:
        El precio total de los precios iniciales una vez aplicada la función a cada uno
    '''
    total_price = 0
    for price in prices_percentages:
        final_price = function(price, prices_percentages[price])
        total_price += final_price
    return total_price
        
basket = {1000:10, 12324:243432, 314324:42, 1:243424214} 
print(return_prices(basket, get_tax))
