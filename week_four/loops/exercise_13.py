# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    user_input = input('>>> INTRODUCE ALGO:\n>>> ')
    
    print(f'>>> {user_input}')
    
    if user_input == 'salir':
        break
