def liste_de_chiffres(chaine: str) -> list[int]:
    """Renvoie la liste des chiffres présents dans `chaine`
    Précondition : aucune
    $$$ liste_de_chiffres('Il fait 7°C et le vent souffle à 10 km/h !')
    [7, 1, 0]
    $$$ liste_de_chiffres("Le 13 mars est le 72e jour d'une année non bissextile.") 
    [1, 3, 7, 2]
    $$$ liste_de_chiffres("Serions-nous le 6 janvier 2022 ?") 
    [6, 2, 0, 2, 2]
    """
    final = []
    for i in chaine:
        if i.isnumeric():
            final.append(i)
    return final


def multiplication(entiers : list[int]) -> int:
    """Renvoie le produit des éléments de `entiers`
    Précondition : aucune
    $$$ multiplication([7, 1, 0])
    0
    $$$ multiplication([1, 3, 7, 2])
    42
    $$$ multiplication([])
    1
    """
    if entiers == []:
        return 1
    first = entiers[0]
    for i in entiers[1::]:
        first *= i
    return first

def contient_une_longueur42(chaines : list[str]) -> bool:
    """ Renvoie `True` si au moins une chaîne de `chaines`
    est de longueur 42, et `False` sinon.
    Précondition : aucune
    $$$ contient_une_longueur42(['Météo.', 'Il fait 7°C et le vent souffle à 10 km/h !'])
    True
    $$$ contient_une_longueur42(['Le Guide du voyageur galactique.', 'Douglas Adams.'])
    False
    $$$ contient_une_longueur42([])
    False
    """
    for elem in chaines:
        if len(elem) == 42:
            return True
    return False
    
def liste_de_phrases(texte : str) -> list[str]:
    """Renvoie la liste des phrases de `texte`.
    Précondition : - `texte` si termine par '.', '?', ou '!'
                   - deux phrases consécutives de `texte` sont séparées par ' '

    >>> liste_de_phrases('Météo. Il fait 7°C et le vent souffle à 10 km/h !')
    ['Météo.', 'Il fait 7°C et le vent souffle à 10 km/h !']    
    >>> liste_de_phrases('Le Guide du voyageur galactique. Douglas Adams.')
    ['Le Guide du voyageur galactique.', 'Douglas Adams.']
    >>> liste_de_phrases("Le 13 mars est le 72e jour d'une année non bissextile.")
    ['Le 13 mars est le 72e jour d'une année non bissextile.']
    """
    phrase = []
    debut = 0
    for i,car in enumerate(texte):
        if car in '.?!':
            phrase.append(texte[debut:i+1])
            



def est_chaine_geek(chaine : str) -> bool:
    """Renvoie vrai si soit la multiplication des chiffres
    que contient `chaine` est égale à 42, soit une des
    phrases qu’elle contient comporte 42 caractères et
    faux dans tous les autres cas.
    Précondition : - `texte` si termine par '.', '?', ou '!'
                   - deux phrases consécutives de `texte` sont séparées par ' '
    $$$ est_chaine_geek('Météo. Il fait 7°C et le vent souffle à 10 km/h !')
    True
    $$$ est_chaine_geek('Le Guide du voyageur galactique. Douglas Adams.')
    False
    $$$ est_chaine_geek("Le 13 mars est le 72e jour d'une année non bissextile.")
    True
    """
    