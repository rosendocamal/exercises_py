# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.

def grades(note):
    try:
        note = float(note)
        if note < 0 or note > 10:
            return 'EN PROCESO'
        if 0 <= note <= 7:
            return 'INSUFICIENTE'
        elif 7 < note <= 8:
            return 'SUFICIENTE'
        elif 8 < note <= 9:
            return 'NOTABLE'
        elif 9 < note < 10:
            return 'EXCELENTE'
        elif note == 10:
            return 'SOBRESALIENTE'
    except ValueError:
        return 'EN PROCESO'

def apply_scores(subjects_and_notes):
    if isinstance(subjects_and_notes, dict):
        return {subject: grades(note) for subject, note in subjects_and_notes.items()}
    else:
        return 'INGRESE LAS CALIFICACIONES CON EL FORMATO DE ASIGNATURA:NOTA EN UN DICCIONARIO'

notes = {'MATEMÁTICAS': 1,
        'GEOGRAFÍA': 10,
        'HISTORIA': 5,
        'CIENCIAS': 7,
        'ARTES': 9}

print(apply_scores(notes))
