def figura(intento):
    if intento == 1:
        return """ +---+
 |   |
     |
     |
     |
     |
========="""
    elif intento == 2:
        return """ +---+
 |   |
 O   |
     |
     |
     |
========="""
    elif intento == 3:
        return """ +---+
 |   |
 O   |
 |   |
     |
     |
========="""
    elif intento == 4:
        return """ +---+
 |   |
 O   |
/|   |
     |
     |
========="""
    elif intento == 5:
        return """ +---+
 |   |
 O   |
/|\  |
     |
     |
========="""
    elif intento == 6:
        return """ +---+
 |   |
 O   |
/|\  |
/    |
     |
========="""
    elif intento == 7:
        return """ +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========="""
    else:
        return "Número de intento no válido"