# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

def apply_function(function, array):
    return [function(x) for x in array]

def square(num):
    return num ** 2

print(apply_function(square, [1, 2, 3, 4]))
