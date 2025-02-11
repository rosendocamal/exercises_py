numero = int(input('INGRESE UN NÚMERO:\n'))

# DETERMINAR SI UN NÚMERO DADO ES NÚMERO PRIMO

def es_numero_primo(numero=1):
    criterio = False
    for i in range(1, numero, 1):
        if numero % i == 0:
            if i != 1 and i != numero:
                criterio = False
                break
            else:
                criterio = True
    return criterio

# GENERAR NÚMEROS PRIMOS HASTA N, SEGÚN INPUT DEL USUARIO

serie_numeros_primos = list()

import time
start = time.time()
for i in range(0, numero, 1):
    if es_numero_primo(i):
        serie_numeros_primos.append(i)

print(serie_numeros_primos)
end = time.time()

print(end - start)
