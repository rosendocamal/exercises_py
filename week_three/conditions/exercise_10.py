'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

    Ingredientes vegetarianos: Pimiento y tofu.
    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

def is_vegetarian():
    print('>>> SELECCIONA UN ÚNICO TIPO DE PIZZA:')
    print('>>> 1) VEGETARIANO\n>>> 2) NO VEGETARIANO')
    while True:
        try:
            option = int(input('>>> '))
            if option == 1 or option == 2:
                break
            else:
                print('>>> INGRESE UNA OPCIÓN VÁLIDA')
        except:
            print('>>> INGRESE UNA OPCIÓN VÁLIDA')
    if option == 1:
        print('>>> HAZ SELECCIONADO PIZZA VEGETARIANA\n>>>')
        return True
    elif option == 2:
        print('>>> HAZ SELECCIONADO PIZZA NO VEGETARIANA\n>>>')
        return False

def get_ingredients(isvegetarian):
    if isvegetarian:
        return 'pimiento', 'tofu'
    else:
        return 'peperoni', 'jamón', 'salmón'

def print_menu(ingredients):
    print('>>> SELECCIONA UN ÚNICO INGREDIENTE:')
    for i in range(0, len(ingredients), 1):
        print(f'>>> {i + 1}) {ingredients[i].upper()}')
    while True:
        try:
            option = int(input('>>> '))
            if 1 <= option <= len(ingredients):
                break
            else:
                print('>>> INGRESE UNA OPCIÓN VÁLIDA')
        except:
            print('>>> INGRESE UNA OPCIÓN VÁLIDA')
    print(f'>>> HAZ SELECCIONADO {ingredients[option - 1].upper()}')
    return ingredients[option - 1]

def print_choose_pizza(isvegetarian, ingredient):
    print('>>>')
    if isvegetarian:
        print('>>> HAZ SELECCIONADO PIZZA VEGETARIANA')
    else:
        print('>>> HAZ SELECCIONADO PIZZA NO VEGETARIANA')
    print('>>> CONTIENE LOS SIGUIENTES INGREDIENTES:')
    print(f'>>> TOMATE, MOZZARELLA, {ingredient.upper()}')
    

def main():
    isvegetarian = is_vegetarian()
    ingredients = get_ingredients(isvegetarian)
    ingredient = print_menu(ingredients)
    menu = print_choose_pizza(isvegetarian, ingredient)

if __name__ == '__main__':
    main()

