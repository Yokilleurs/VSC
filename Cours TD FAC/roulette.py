# TP 4 : roulette
# NOM1 Prénom1
# NOM2 Prénom2
# PEIP 1X

def represente_entier(chaine : str) -> bool:
    """Renvoie `True` si et seulement si `chaine` est une représentation
    littérale valide en base 10 d'un entier positif ou nul en python.
    Précondition : /
    Exemples :
    >>> represente_entier("42")
    True
    >>> represente_entier("quarante-deux")
    False
    >>> represente_entier("3.0")
    False
    >>> represente_entier("-5")
    False
    >>> represente_entier("1+1")
    False
    >>> represente_entier("2B")
    False
    """
    return chaine.isnumeric()

# Question 8
# Essayez de ne pas utiliser de if dans cette question.

def pari_valide(pari: str) -> bool:
    """Renvoie `True` si `pari` :
     - est 'passe' ou 'manque' ;
     - ou est 'paire' ou 'impaire' ;
     - ou est 'rouge' ou 'noire' ;
     - ou représente un nombre entier compris entre 1 et 36 inclus
    et `False` sinon.
    Précondition: /
    Exemples :
    >>> pari_valide("passe")
    True
    >>> pari_valide("vert")
    False
    >>> pari_valide("12")
    True
    >>> pari_valide("8")
    True
    >>> pari_valide("0")
    False
    >>> pari_valide("42")
    False
    """
    return (pari == "passe" or pari == "manque"
           or pari == "paire" or pari == "impaire"
           or pari == "rouge" or pari == "noire"
           or represente_entier(pari) and 1 <= int(pari) <= 36)

# Question 9

import random

# vous ne vous souvenez plus de la fonction du module `random` renvoyant
# un entier (`int`) aléatoire (`rand`…) ? Utilisez `dir(random)` pour obtenir
# la liste de toutes les fonctions du module `random` puisr
# `help(random.randint)` pour afficher la documentation de cette fonction.
# Oups, j'ai accidentellement rappelé son nom.

def tirage_roulette() -> int:
    """Renvoie un entier aléatoire tiré uniformément entre 0 et 36.
    Précondition : /
    Pas d'exemples (c'est aléatoire !)
    """
    return random.randint(0, 36)

# Question 10

def somme_chiffres(n: int) -> int:
    """Renvoie la somme des chiffres de `n`.
    Précondition : 0 <= n < 100
    Exemples :
    >>> somme_chiffres(42)
    6
    >>> somme_chiffres(7)
    7
    """
    return n // 10 + n % 10

# Question 11

def couleur_case(n: int) -> str:
    """Renvoie la couleur qu’aurait une case numérotée par `n`
    à la roulette.
    Précondition : 0 <= n <= 36
    >>> couleur_case(4)
    'noire'
    >>> couleur_case(0)
    'verte'
    >>> couleur_case(12)
    'rouge'
    >>> couleur_case(10)
    'noire'
    >>> couleur_case(28)
    'noire'
    """
    if n == 0:
        couleur = "verte"
    elif n == 10 or n == 18 or somme_chiffres(n) % 2 == 0:
        couleur = "noire"
    else:
        couleur = "rouge"
    return couleur

# Question 12

# Astuce : commencez par le cas dans lequel la boule tombe sur le 0

def gains_roulette(pari: str, mise: int, case: int) -> int:
    """Renvoie le gain obtenu par un joueur ayant parié sur `pari` et misé
    `mise` lorsque la bille s’est arrêtée sur `case`.
    Précondition : - `pari` est un pari valide
                   - mise > 0
                   - 0 <= case <= 36
    >>> gains_roulette("paire", 10, 14)
    20
    >>> gains_roulette("paire", 10, 19)
    0
    >>> gains_roulette("paire", 10, 0)
    0
    >>> gains_roulette("impaire", 10, 14)
    0
    >>> gains_roulette("impaire", 10, 19)
    20
    >>> gains_roulette("manque", 10, 14)
    20
    >>> gains_roulette("manque", 10, 19)
    0
    >>> gains_roulette("manque", 10, 0)
    0
    >>> gains_roulette("passe", 10, 14)
    0
    >>> gains_roulette("passe", 10, 19)
    20
    >>> gains_roulette("noire", 10, 14)
    0
    >>> gains_roulette("noire", 10, 19)
    20
    >>> gains_roulette("noire", 10, 0)
    0
    >>> gains_roulette("rouge", 10, 14)
    20
    >>> gains_roulette("rouge", 10, 19)
    0
    """
    if case == 0:
        gains = 0
    elif (pari == "paire" and case % 2 == 0
          or pari == "impaire" and case % 2 == 1
          or pari == "passe" and case >= 19
          or pari == "manque" and case <= 18
          or pari == couleur_case(case)):
        gains = mise * 2
    elif pari == str(case):
        gains = mise * 36
    else:
        gains = 0
    return gains

import doctest
doctest.testmod()



