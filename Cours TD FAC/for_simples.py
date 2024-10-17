# Exercices sur les boucles for

# Attention ! Ne pas utiliser d'indices !

## Accumulation simple

def nombre_pairs(entiers: list[int]) -> int:
    """Renvoie le nombre de nombres pairs dans la liste `entiers`
    Précondition : aucune
    Exemple(s) :
    $$$ nombre_pairs([1, 3, 4, 9, 10])
    2
    $$$ nombre_pairs([3])
    0
    $$$ nombre_pairs([])
    0
    """
    nb_nb_pair = 0
    for i in entiers:
        if i % 2 == 0:
            nb_nb_pair += 1
    return nb_nb_pair

# déjà donné, rien à faire pour ce prédicat
def est_chiffre(caractere: str) -> bool:
    """Renvoie `True` si `caractere` est un chiffre, et `False` sinon.
    Précondition : len(caractere) == 1
    Exemple(s) :
    $$$ est_chiffre('3')
    True
    $$$ est_chiffre('Z')
    False
    """
    return caractere.isdigit()

def nombre_chiffres(chaine: str) -> int:
    """Renvoie le nombre de chiffres dans la chaîne passée en paramètre.

    Précondition : 
    Exemple(s) :
    $$$ nombre_chiffres("24 heures")
    2
    $$$ nombre_chiffres("douze")
    0
    $$$ nombre_chiffres("")
    0
    """
    nb_nb_pair = 0
    for caractere in chaine:
        if est_chiffre(caractere) and caractere%2 == 0:
            nb_nb_pair += 1
    return nb_nb_pair



def produit(entiers: list[int]) -> int:
    """Renvoie le produit des nombres de la liste `entiers`
    Précondition : aucune
    Exemple(s) :
    $$$ produit([2, 3, 7])
    42
    $$$ produit([])
    1
    """
    pd = 1
    for i in entiers:
        pd = pd * i
    return pd


## Application de fonction sur un itérable

def double(entiers: list[int]) -> list[int]:
    """Renvoie la liste contenant le double de chacun des
    éléments de `entiers`.
    Précondition : aucune
    Exemple(s) :
    $$$ double([1, 4, 9])
    [2, 8, 18]
    $$$ double([])
    []
    """
    return [i*2 for i in entiers]


def censure_chiffres(chaine: str) -> str:
    """Renvoie une chaîne identique à `chaine`, mais avec les chiffres
    remplacés par `*`
    Précondition : aucune
    Exemple(s) :
    $$$ censure_chiffres("Mon numéro de carte bleue est le 5133 7931 8421 3924.")
    'Mon numéro de carte bleue est le **** **** **** ****.'
    $$$ censure_chiffres("x=c^d[mod N]")
    'x=c^d[mod N]'
    $$$ censure_chiffres('')
    """
    redacted = ''
    for caractere in chaine:
        if est_chiffre(caractere):
            redacted += '*'
        else:
            redacted += caractere
    return redacted

## Filtre

def positifs_et_pairs(entiers: list[int]) -> list[int]:
    """Renvoie la liste des nombres positifs ou nuls et pairs de `entiers`.
    Précondition : aucune
    Exemple(s) :
    $$$ positifs_et_pairs([1, -2, -3, 4, 0, -6])
    [4, 0]
    $$$ positifs_et_pairs([-2, 3])
    []
    $$$ positifs_et_pairs([])
    []
    """
    liste_triee = []
    for i in entiers:
        if i >= 0 and i % 2 == 0:
            liste_triee.append(i)
    return liste_triee

def suppression_caractere(chaine: str, carac: str) -> str:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : len(carac) == 1
    Exemple(s) :
    $$$ suppression_caractere("Salut tu vas bien ?", ' ')
    'Saluttuvasbien?'
    $$$ suppression_caractere("Bonjour", 'e')
    'Bonjour'
    $$$ suppression_caractere("", 'x')
    ''
    """
    corrected = ''
    for caractere in chaine:
        if caractere != carac:
            corrected += caractere
    return corrected

