'''
En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel: 	Puntuación
Inaceptable: 	0.0
Aceptable: 	0.4
Meritorio: 	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''

SCORE_UNACCEPTABLE = 0.0
SCORE_ACCEPTABLE = 0.4
SCORE_MERITORIUS = 0.6
SCORE_REWARD = 2400

def get_score():
    while True:
        try:
            score = float(input(f'>>> INGRESE SU PUNTUACIÓN ({SCORE_UNACCEPTABLE}, {SCORE_ACCEPTABLE}, {SCORE_MERITORIUS} O MÁS):\n>>> '))
            if score == SCORE_UNACCEPTABLE or score == SCORE_ACCEPTABLE or score >= SCORE_MERITORIUS:
                return score
            else:
                print(f'>>> ERROR: NÚMERO NO PERMITIDO. INGRESE {SCORE_UNACCEPTABLE}, {SCORE_ACCEPTABLE}, U OTRA PUNTUACIÓN MAYOR O IGUAL QUE {SCORE_MERITORIUS}')
        except ValueError:
            print('>>> ERROR: POR FAVOR INGRESE UN NÚMERO VÁLIDO')

def get_level(score):
    if score == SCORE_UNACCEPTABLE:
        return 'INACEPTABLE'
    elif score == SCORE_ACCEPTABLE:
        return 'ACEPTABLE'
    elif score >= SCORE_MERITORIUS:
        return 'MERITORIO'

def get_money(score):
   return round(score * SCORE_REWARD, 2)

def main():
    score = get_score()
    level = get_level(score)
    money = get_money(score)
    print(f'>>> SU NIVEL DE RENDIMIENTO ES {level} Y LE CORRESPONDE POR ELLO ${money}')

if __name__ == '__main__':
    main()
