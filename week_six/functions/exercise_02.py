# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def get_name():
    while True:
        name = input('>>> INGRESE UN ÚNICO NOMBRE:\n>>> ').strip()
        if name.isalpha():
            return name.capitalize()
        else:
            print('>>> ERROR: POR FAVOR, INGRESE UN ÚNICO NOMBRE VÁLIDO')

def show_name(name):
    print(f'>>> ¡Hola {name}!')

def main():
    name = get_name()
    show_name(name)

if __name__ == '__main__':
    main()
