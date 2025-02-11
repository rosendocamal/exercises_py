# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

from exercise_01 import subjects

list_subjects = subjects()
list_notes = []

def read_note(subject):
    while True:
        try:
            note = float(input(f'CALIFICACIÓN EN {subject.upper()}:\n'))
            if 0 <= note <= 10:
                return note
            else:
                print('ERROR: INGRESE UNA CALIFICACIÓN ENTRE 0 Y 10')
        except ValueError:
            print('ERROR: POR FAVOR, INGRESE UNA NOTA VÁLIDA ENTRE 0 Y 10')

def print_notes(notes, subjects):
    for i in range(len(subjects)):
        print(f'EN {subjects[i].upper()} HAS SACADO {notes[i]}')
   
def main():
    for subject in list_subjects:
        list_notes.append(read_note(subject))

    if isinstance(list_notes, list) and isinstance(list_subjects, list):
        if len(list_notes) == len(list_subjects):
            print_notes(list_notes, list_subjects)
        else:
            print('ERROR: DATOS CORROMPIDOS, LA CANTIDAD DE NOTAS NO COINCIDEN CON LA CANTIDAD DE ASIGNATURAS')
    else:
        print('ERROR: DATOS ALMACENADOS DE FORMA INCORRECTA, VERIFIQUE LAS NOTAS Y ASIGNATURAS SEAN DEL TIPO LISTAS')

if __name__ == '__main__':
    main()
