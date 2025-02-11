# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

COST_FREE = 0
COST_CHILD = 5
COST_ADULT = 10

AGE_CHILD_MIN = 4
AGE_CHILD_MAX = 18
AGE_ADULT_MIN = 19

def get_age():
    while True:
        try:
            age = int(input('>>> INGRESE SU EDAD:\n>>> '))
            if 0 <= age <= 130:
                return age
            else:
                print('>>> ERROR: INGRESE UNA EDAD VÁLIDA ENTRE 0 Y 130')
        except ValueError:
            print('>>> ERROR: POR FAVOR INGRESE UN NÚMERO ENTERO VÁLIDO COMO EDAD')

def get_cost(age):
    if age < AGE_CHILD_MIN:
        return COST_FREE
    elif AGE_CHILD_MIN <= age <= AGE_CHILD_MAX:
        return COST_CHILD 
    elif age >= AGE_ADULT_MIN:
        return COST_ADULT

def main():
    age = get_age()
    cost = get_cost(age)

    if cost == COST_FREE:
        print('>>> ENTRADA GRATUITA')
    else:
        print(f'>>> COSTO DEL BOLETO: ${cost}')

if __name__ == '__main__':
    main()
