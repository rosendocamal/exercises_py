'''
Ejercicio 4: Ordenar y Filtrar Lista de Números

Descripción:

Crea un programa que pida al usuario una lista de números enteros separados por comas. El programa debe:

Ordenar la lista en orden ascendente.
Filtrar los números para que solo queden aquellos que sean múltiplos de 3.
Mostrar la lista resultante.

Requerimientos:

Utiliza métodos de listas como sort(), filter(), o comprensión de listas.
Asegúrate de manejar adecuadamente la entrada del usuario para convertirla en una lista de números enteros.
Ejemplo de entrada: 1, 2, 3, 6, 7, 9 → Salida: [3, 6, 9]
'''

def read_input():
    while True:
        input_num = input('>>> INGRESE UNA LISTA DE NÚMEROS ENTEROS POSITIVOS SEPARADOS POR COMAS:\n>>> EJEMPLO: 1, 2, 3, 6, 7, 9\n>>> ')
        nums = ''.join(input_num.split(' ')).split(',')
        
        try:    
            serie_nums = list(int(num) for num in nums)
            # for num in nums:
            #    serie_nums.append(int(num))
            return serie_nums
        except:
            print('>>> VERIFIQUE LOS DATOS INGRESADOS. INGRESE NÚMEROS ENTEROS POSITIVOS PARA CONTINUAR\n>>>\n')
        

list_numbers = read_input()

def is_multiple_three(num):
    if num % 3 == 0:
        return True
    else:
        return False

multiple_three = list()

for multiple in filter(is_multiple_three, list_numbers):
    multiple_three.append(multiple)

multiple_three.sort()
print(multiple_three)

