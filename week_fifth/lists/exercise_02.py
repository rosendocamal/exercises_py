# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

from exercise_01 import subjects

subjects = subjects()
for subject in subjects:
    print(f'YO ESTUDIO {subject.upper()}')
