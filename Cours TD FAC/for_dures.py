# Exercices sur les boucles for

# Attention ! Ne pas utiliser d'indices !

# Facultatif

def sommes_cumulees(entiers:list[int]) -> list[int]:
    """Renvoie la liste des sommes cumulées des éléments de `entiers`
    Précondition : Aucune
    Exemple(s) :
    $$$ sommes_cumulees([1, 5, 10])
    [1, 6, 16]
    $$$ sommes_cumulees([1, 10, 100])
    [1, 11, 111]
    """
    j = 0
    liste_somme = []
    for i in entiers:
        somme = j + i
        j += i
        liste_somme.append(somme)
    return liste_somme


def decoupe_chaine(chaine: str, separateur: str) -> list[str]:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : len(separateur) == 1
    Exemple(s) :
    $$$ decoupe_chaine("18/10/2023", '/')
    ['18', '10', '2023']
    $$$ decoupe_chaine("abba", 'b')
    ['a', '', 'a']
    $$$ decoupe_chaine("abba", 'a')
    ['', 'bb', '']
    """
    liste_separee = []
    chaine_temp = ''
    for caractere in chaine:
        if caractere != separateur:
            chaine_temp += caractere
        elif caractere == separateur:
            liste_separee.append(chaine_temp)
            chaine_temp = ''
    liste_separee.append(chaine_temp)
    return liste_separee

def description(chaine: str) -> list[tuple[str, int]]:
    """renvoie une liste de couples (caractère, entier) correspondant
    aux caractères de `chaine` et aux nombres d'occurences consécutives
    de ces caractères.
    Précondition: aucune
    $$$ description("abba")
    [('a', 1), ('b', 2), ('a', 1)]
    $$$ description("ddddaadddaaa")
    [('d', 4), ('a', 2), ('d', 3), ('a', 3)]
    """
    if chaine == '': raise TypeError("arg must not be empty")
    liste_occu = []
    carac_pre = 0
    n = 0
    for caractere in chaine:
        if carac_pre == 0 or carac_pre == caractere:
            n += 1
            carac_pre = caractere
            tuple_temp = (caractere, n)
        else:
            n = 1
            carac_pre = caractere
            liste_occu.append(tuple_temp)
            tuple_temp = (caractere, n)
    liste_occu.append(tuple_temp)
    return liste_occu


def reconstitution(liste_couples: list[tuple[str, int]]) -> str:
    """réciproque de `description`
    Précondition : tous les seconds éléments des éléments de `liste_couples` sont > 0.
    Exemple(s) :
    $$$ reconstitution([('a', 1), ('b', 2), ('a', 1)])
    'abba'
    $$$ reconstitution([('d', 4), ('a', 2), ('d', 3), ('a', 3)])
    'ddddaadddaaa'
    """
    chaine_recon = ''
    for (a,b) in liste_couples:
        chaine_recon += a*b
    return chaine_recon