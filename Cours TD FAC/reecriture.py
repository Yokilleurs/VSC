def reecriture_lettre(lettre : str) -> str:
    if lettre == 'a':
        trans = 'bc'
    elif lettre == 'b':
        trans = 'a'
    elif lettre == 'c':
        trans = 'aaa'
    else:
        trans = lettre
    return trans

def reecriture_mot(mot:str)-> str:
    return mot[2:] + reecriture_lettre(mot[0])

def nbre_reecritures(mot:str)->int:
    iteration = 0
    while mot != 'a':
        mot = reecriture_mot(mot)
        iteration += 1
    return iteration