'''
Ejercicio 6: Reemplazar Subcadenas en una Lista de Cadenas

Descripción:

Crea un programa que tenga una lista de frases y reemplace una subcadena específica en cada frase. El programa debe pedir al usuario la subcadena a buscar y la subcadena de reemplazo, y luego aplicar ese reemplazo en todas las frases de la lista.

Requerimientos:

Utiliza los métodos de cadenas como replace() para hacer el reemplazo.
La lista de frases debe ser predefinida.
El programa debe devolver la lista de frases modificadas con el reemplazo realizado.

Ejemplo:
    frases = ["El cielo es azul", "La tierra es verde", "El mar es azul"]
    # Si el usuario ingresa "azul" como la subcadena a buscar y "rojo" como reemplazo
    # El resultado debería ser: ["El cielo es rojo", "La tierra es verde", "El mar es rojo"]
'''

phrases = ['El cielo es azul', 'La tierra es verde', 'El mar es azul']
modified_phrases = []

msg_error = '>>> ¡ERROR! INGRESA UNA CADENA VÁLIDA PARA CONTINUAR'
while True:
    substring = input('>>> INGRESA UNA SUBCADENA A BUSCAR:\n>>> ')
    if substring != '':
        break
    else:
        print(msg_error)

while True:
    substring_replacement = input(f'>>> REMPLAZAR "{substring}" POR:\n>>> ')
    if substring_replacement != '':
        break
    else:
        print(msg_error)

for phrase in phrases:
    modified_phrases.append(phrase.replace(substring, substring_replacement))

print(modified_phrases)
