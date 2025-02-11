import math

# Validar ingreso de cualquier entrada de datos por parte del usuario sea únicamente valores enteros positivos mayores a 0 y también validar los errores.

evento_error = False

try:
    numero_determinar_criterio_divisibilidad = 0
    while numero_determinar_criterio_divisibilidad < 1:
        numero_determinar_criterio_divisibilidad = int(input('\nINGRESE UN NÚMERO ENTERO POSITIVO: ')) 
except ValueError:
    print('\nERROR: INGRESE ÚNICAMENTE NÚMEROS ENTEROS POSITIVOS, NO AÑADA "+", "," Y "." NI OTROS SIGNOS Y LETRAS')
    evento_error = True
except:
    print('\nHA OCURRIDO UN ERROR INESPERADO. ESTAMOS TRABAJANDO EN ELLO')
    evento_error = True
else: 
    print('\n')
    numero_cifras = []
    for i in range(len(str(numero_determinar_criterio_divisibilidad))):
        numero_cifras.append(int(str(numero_determinar_criterio_divisibilidad)[i]))
    mensaje_criterio_divisibilidad = 'DIVISIBLE ENTRE '
    if len(numero_cifras) >= 1:
        numero_cifra_ultima = numero_cifras[len(numero_cifras) - 1]
    if len(numero_cifras) >= 2:
        numero_cifra_penultima = numero_cifras[len(numero_cifras) - 2]
    if len(numero_cifras) >= 3:
        numero_cifra_antepenultima = numero_cifras[len(numero_cifras) - 3]

    # Divisible entre 2: Entero termina en 0, 2, 4, 6 u 8, son números pares.

    def determinar_divisibilidad_dos():
        if numero_cifra_ultima == 0:
            return mensaje_criterio_divisibilidad + ' 2'
        elif numero_cifra_ultima == 2:
            return mensaje_criterio_divisibilidad + ' 2'
        elif numero_cifra_ultima == 4:
            return mensaje_criterio_divisibilidad + ' 2'
        elif numero_cifra_ultima == 6:
            return mensaje_criterio_divisibilidad + ' 2'
        elif numero_cifra_ultima == 8:
            return mensaje_criterio_divisibilidad + ' 2'
        else:
            return 'NO ES {} 2'.format(mensaje_criterio_divisibilidad)

    print(determinar_divisibilidad_dos())

    # Divisible entre 3: Suma de los dígitos es igual a un múltiplo de 3.

    def determinar_divisibilidad_tres():
        suma_digitos = 0
        for cifra in numero_cifras:
            suma_digitos += cifra
        if suma_digitos % 3 == 0:
            return '{} 3'.format(mensaje_criterio_divisibilidad)
        else:
            return 'NO ES {} 3'.format(mensaje_criterio_divisibilidad)

    print(determinar_divisibilidad_tres())

    # Divisible entre 4: Si los últimos 2 dígitos son 0 o un múltiplo de 4.

    if len(numero_cifras) > 2:
        if numero_cifra_ultima == 0 and numero_cifra_penultima == 0:
            print(mensaje_criterio_divisibilidad + ' 4')
        elif (numero_cifra_penultima * 10 + numero_cifra_ultima) % 4 == 0:
            print(mensaje_criterio_divisibilidad + ' 4')
        else:
            print('NO ES ' + mensaje_criterio_divisibilidad + ' 4')
    elif numero_cifra_ultima % 4 == 0:
        print(mensaje_criterio_divisibilidad + ' 4')
    else:
        print('NO ES ' + mensaje_criterio_divisibilidad + ' 4')


    # Divisible entre 5: Si el último dígito termina en 0 o 5.

    if numero_cifra_ultima == 0 or numero_cifra_ultima == 5:
        print(mensaje_criterio_divisibilidad + ' 5')
    else:
        print('NO ES ' + mensaje_criterio_divisibilidad + ' 5')

    # Divisible entre 6: Si es divisible entre 2 y 3.

    if determinar_divisibilidad_dos() == '{} 2'.format(mensaje_criterio_divisibilidad) and determinar_divisibilidad_tres() == '{} 3'.format(mensaje_criterio_divisibilidad):
        print(mensaje_criterio_divisibilidad + ' 6')
    else:
            print('NO ES ' + mensaje_criterio_divisibilidad + ' 6')

    # Divisible entre 7: El último dígito se multiplica por 2 y el producto se le resta a los dígitos restantes y continuar así hasta que la diferencia solo tenga 2 cifras. Cuya diferencia debe ser 0 o múltiplo de 7.

    criterio_divisibilidad_siete = abs(math.trunc(numero_determinar_criterio_divisibilidad / 10) - numero_cifra_ultima * 2)

    def numero_digitos_lista():
        criterio_divisibilidad_siete_cifras = []
        for i in range(len(str(criterio_divisibilidad_siete)) - 1):
            criterio_divisibilidad_siete_cifras.append(int(str(criterio_divisibilidad_siete)[i]))
        return criterio_divisibilidad_siete_cifras

    def determinar_divisibilidad_siete():
        if criterio_divisibilidad_siete == 0 or criterio_divisibilidad_siete % 7 == 0:                
            print(mensaje_criterio_divisibilidad + ' 7')
        else:                                                                                         
            print('NO ES {} 7'.format(mensaje_criterio_divisibilidad))

    if len(numero_digitos_lista()) > 2:
        while len(numero_digitos_lista()) == 2:
            criterio_divisibilidad_siete = math.trunc(criterio_divisibilidad_siete / 10) - int(str(criterio_divisibilidad_siete)[len(str(criterio_divisibilidad_siete)) - 1])
            numero_digitos_lista()
        determinar_divisibilidad_siete()
    else:
        determinar_divisibilidad_siete()

    # Divisible entre 8: Si los últimos 3 dígitos son 0 o un múltiplo de 8.

    if len(numero_cifras) >= 3:
        if numero_cifra_antepenultima == 0 and numero_cifra_penultima == 0 and numero_cifra_ultima == 0:
            print(mensaje_criterio_divisibilidad + ' 8')
        else:
            if (numero_cifra_antepenultima * 100 + numero_cifra_penultima * 10 + numero_cifra_ultima) % 8 == 0:
                print(mensaje_criterio_divisibilidad + ' 8')
            else:
                print('NO ES ' + mensaje_criterio_divisibilidad + ' 8')
    elif 1 <= len(numero_cifras) < 3:
        if numero_determinar_criterio_divisibilidad % 8 == 0:
            print(mensaje_criterio_divisibilidad + ' 8')
        else:
            print('NO ES ' + mensaje_criterio_divisibilidad + ' 8')


    # Divisible entre 9: La suma de los dígitos es múltiplo de 9.

    suma_digitos = 0
    for cifra in numero_cifras:
        suma_digitos += cifra
    if suma_digitos % 9 == 0:
        print(mensaje_criterio_divisibilidad + ' 9')
    else:
        print('NO ES ' + mensaje_criterio_divisibilidad + ' 9')

    # Divisible entre 10: El último dígito es 0.

    if numero_cifra_ultima == 0:
        print(mensaje_criterio_divisibilidad + ' 10')
    else:
        print('NO ES ' + mensaje_criterio_divisibilidad + ' 10')

    # Divisible entre 11: El valor absoluto de la diferencia entre la suma de los dígitos en posición par y la suma de los dígitos en posición impar es 0 o múltiplo de 11

    numero_cifras_posicion_par = 0
    numero_cifras_posicion_impar = 0

    for i in range(0, len(numero_cifras), 1):
        if (i + 1) % 2 != 0:
            numero_cifras_posicion_impar += numero_cifras[i]
        else:
            numero_cifras_posicion_par += numero_cifras[i]
    if abs(numero_cifras_posicion_par - numero_cifras_posicion_impar) == 0 or abs(numero_cifras_posicion_par - numero_cifras_posicion_impar) % 11 == 0: 
        print(mensaje_criterio_divisibilidad + ' 11')
    else:
        print('NO ES ' + mensaje_criterio_divisibilidad + ' 11')

    # Divisibilidad entre 13: Multiplicar el último dígito por 9 y restar el producto al número que se forma con las cifras restantes, la diferencia es 0 o múltiplo de 13

    suma_digitos = 0

    for i in range(0, len(numero_cifras) - 1, 1):
        suma_digitos += numero_cifras[i] * 10 ** (len(numero_cifras) - (2 + i))

    if suma_digitos - (numero_cifras[len(numero_cifras) - 1] * 9) == 0 or suma_digitos - (numero_cifras[len(numero_cifras) - 1] * 9) % 13 == 0:
        print(mensaje_criterio_divisibilidad + ' 13')
    else:
        print('NO ES ' + mensaje_criterio_divisibilidad + ' 13')

    # Divisibilidad entre 19: Si al último dígito multiplicado por 17 y restar el producto al número que se forma con las cifras restantes, la diferencia es 0 múltiplo de 19

    suma_digitos = 0                   

    for i in range(0, len(numero_cifras) - 1, 1):    
        suma_digitos += numero_cifras[i] * 10 ** (len(numero_cifras) - (2 + i))

    if suma_digitos - (numero_cifras[len(numero_cifras) - 1] * 17) == 0 or suma_digitos - (numero_cifras[len(numero_cifras) - 1] * 17) % 19 == 0:    
        print(mensaje_criterio_divisibilidad + ' 19')
    else:                          
            print('NO ES ' + mensaje_criterio_divisibilidad + ' 19')
    #evento_error = False

finally:
    if evento_error == False:
        print('\nGRACIAS POR UTILIZARME\n')
    else:
        print('\nLO SENTIMOS. REINICIE EL PROGRAMA\n')
