# Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

def grade(note):
    if note < 0:
        return 'REPROBADO'
    if note > 10:
        return 'SOBRESALIENTE'

    if 0 <= note <= 5:
        return 'REPROBADO'
    elif 5 < note <= 6:
        return 'REGULAR'
    elif 6 < note <= 7:
        return 'BIEN'
    elif 7 < note <= 8:
        return 'MUY BIEN'
    elif 8 < note <= 9:
        return 'EXCELENTE'
    elif 9 < note <= 10:
        return 'SOBRESALIENTE'

def apply_score(list_notes):
    return [grade(i) for i in list_notes]

print(apply_score([1, 2, 3, 0, 13, 1, 2, 3, 4, 5, 6, 7, 6, 8, 1, 10, 9]))
