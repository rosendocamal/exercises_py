# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

score_per_subject = { 
        'matemáticas': 6,
        'física': 4,
        'química': 5,
        'historia': 8,
        'lengua': 10
        }

total_score = 0

for subject in score_per_subject:
    score = score_per_subject[subject]
    total_score += score
    print(f'>>> {subject.upper()} TIENE {score} CRÉDITOS')

print(f'>>> {total_score} DE CRÉDITOS OBTENIDOS')
