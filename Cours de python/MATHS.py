from math import *
def delta(a, b, c):
    resultat = b**2 - 4*a*c
    if resultat == 0:
        print("Il y a une solution")
    elif resultat < 0:
        print("Il n'y a pas de solution")
    else:
        print("Il y a deux solutions")
    return resultat