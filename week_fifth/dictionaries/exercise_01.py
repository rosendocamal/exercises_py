# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

foreign_exchange = {
        'Euro': '€',
        'Dollar': '$',
        'Yen': '¥'
        }

while True:
    user_currency = input('>>> INGRESE UNA DIVISA:\n>>> ').strip().capitalize()
    if user_currency and foreign_exchange.get(user_currency) != None:
        print(f'>>> {foreign_exchange[user_currency]}')
        break
    else:
        print(f'>>> LA DIVISA "{user_currency.upper()}" NO SE ENCUENTRA EN EL REGISTRO')
