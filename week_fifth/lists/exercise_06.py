# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

from exercise_01 import subjects

NOTE_MAX = 10
NOTE_MIN = 0
NOTE_MIN_APPROVING = 5

def get_notes(subjects):
    notes = []
    for subject in subjects:
        while True:
            try:
                note = float(input(f'>>> INGRESE SU NOTA DE {subject.upper()}:\n>>> '))
                if NOTE_MIN <= note <= NOTE_MAX:
                    notes.append(note)
                    break
                else:
                    print(f'>>> ERROR: INGRESE UNA NOTA VÁLIDA ENTRE {NOTE_MIN} Y {NOTE_MAX}')
            except ValueError:
                print(f'>>> ERROR: POR FAVOR INGRESE UN NÚMERO VÁLIDO COMO NOTA ENTRE {NOTE_MIN} Y {NOTE_MAX}')
    return notes

def get_failed_subjects(subjects, notes):
    total_subjects = len(subjects)
    failed_subjects = subjects.copy()
    for i in range(total_subjects):
        if notes[i] >= NOTE_MIN_APPROVING:
            failed_subjects.remove(subjects[i])
    return failed_subjects

def show_failed_subjects(failed_subjects):
    if len(failed_subjects) >= 1:
        return f'>>> ASIGNATURA(S) REPROBADA(S): {", ".join(failed_subjects).upper()}'
    return '>>> NO CUENTAS CON ASIGNATURAS REPROBADAS'

def main():
    list_subjects = subjects()
    notes = get_notes(list_subjects)
    failed_subjects = get_failed_subjects(list_subjects, notes)
    
    print(show_failed_subjects(failed_subjects))

if __name__ == '__main__':
    main()
