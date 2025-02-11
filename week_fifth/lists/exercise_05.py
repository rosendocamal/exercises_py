# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for i in range(0, len(numbers)):
    if i != len(numbers) - 1:
        print(numbers[i], end=', ')
    else:
        print(numbers[i])
