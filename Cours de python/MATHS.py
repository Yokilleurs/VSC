from math import *
def delta(a, b, c):
    resultat = b**2 - 4*a*c
    if resultat == 0:
        print("delta =", resultat)
        print("Il y a une solution")
        x1 = (-b-sqrt(resultat))/(2*a)
        print("x1 =", x1)
    elif resultat < 0:
        print("delta =", resultat)
        print("Il n'y a pas de solution")
    else:
        print("Il y a deux solutions")
        x1 = (-b-sqrt(resultat))/(2*a)
        x2 = (-b+sqrt(resultat))/(2*a)
        print("delta =", resultat)
        print("x1    =", x1)
        print("x2    =", x2)
    return  