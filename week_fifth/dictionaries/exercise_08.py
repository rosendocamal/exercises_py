# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.

spanish_to_english = {}

def get_translations():
    while True:
        translations = input('>>> INGRESE LAS TRADUCCIONES CON EL FORMATO "palabra:traducción" Y SEPARADOS POR COMA:\n>>> ')
        
        translation_per_word = translations.split(',')
        total_separators_index = 0
        for i in translation_per_word:
            separator_index = i.find(':')
            if separator_index != -1:
                total_separators_index += 1 

        if translations != '' and total_separators_index == len(translation_per_word):
            for i in translation_per_word:
                separator_index = i.find(':')
                word_in_spanish = i[:separator_index].strip()
                english_translation = i[separator_index + 1:].strip()
                
                if word_in_spanish.isalpha() and english_translation.isalpha():
                    spanish_to_english.update({word_in_spanish: english_translation})
            break
        else:
            print('>>> ERROR: INGRESE LA TRADUCCIÓN CON EL FORMATO "palabra:traducción" PARA CONTINUAR Y SEPARELOS POR COMAS')

def get_phrase_in_spanish():
    while True:
        phrase = input('>>> INGRESE UNA FRASE EN ESPAÑOL PARA TRADUCIRLA AL INGLÉS:\n>>> ').strip()
        if phrase != '':
            return phrase
        else:
            print('>>> ERROR: POR FAVOR, INGRESE UNA FRASE EN ESPAÑOL PARA TRADUCIRLA AL INGLÉS')

def get_translation_phrase(phrase):
    for word in spanish_to_english.keys():
        if word in phrase.lower():
            translated_phrase = phrase.replace(word, spanish_to_english[word])
        phrase = translated_phrase

    return translated_phrase

def main():
    get_translations()
    phrase = get_phrase_in_spanish()
    translated_phrase = get_translation_phrase(phrase.lower())
    
    print(f'>>> {translated_phrase.upper()}')

if __name__ == '__main__':
    main()
