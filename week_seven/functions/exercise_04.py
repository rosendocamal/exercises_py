# Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

def apply_boolean(function, array):
    return [i for i in array if function(i)]

def par(n):
    return n % 2 == 0

print(apply_boolean(par, [1, 2, 3, 4, 5, 6, 7, 8]))
