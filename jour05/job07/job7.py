def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_superieur = ((note + 4) // 5) * 5
            if multiple_de_5_superieur - note < 3:
                notes_arrondies.append(multiple_de_5_superieur)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

notes = [38, 82, 65, 91, 43]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)
