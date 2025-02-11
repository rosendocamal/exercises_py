# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.

def grade(note):
    try:
        if float(note) >= 6:
            return 'APROBADO'
    except ValueError:
        pass

def apply_score(subjects_notes):
    if isinstance(subjects_notes, dict):
        return {subject: grade(note) for subject, note in subjects_notes.items() if bool(grade(note))}
   
sn = {'MATH': 5,
        'GEOGRAFÍA': 7,
        'LOPÉZ': 8,
        'JUAN': 4}

print(apply_score(sn))
