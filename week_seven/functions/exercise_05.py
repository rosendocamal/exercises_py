# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def request_entry(msg):
    return input(msg)

def is_valid_string(string):
    return bool(string)

def request_valid_entry(msg, validator):
    entry = request_entry(msg)
    if validator(entry):
        return entry
    else:
        print('>>> REINTENTE DE NUEVO')
        return request_entry(msg, validator)

def main():
    phrase = request_valid_entry('>>> INGRESE UNA FRASE:\n>>> ', is_valid_string).split()
    return {word: len(word) for word in phrase}

print(main())

