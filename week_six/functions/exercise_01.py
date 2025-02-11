# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def greet():
    print('¡HOLA AMIGA!')

counter = 0
while True:
    counter += 1
    print(counter, end='. ')
    greet()
