def nouvelle_grille(hauteur:int, largeur:int)->list[list[int]]:
    """Renvoie une liste de `hauteur` listes de `largeur` 0 représentant
    une grille vide
    Précondition : hauteur > 0 et largeur > 0
    $$$ g = nouvelle_grille(3, 4)
    $$$ g
    [[0, 0, 0, 0], \
     [0, 0, 0, 0], \
     [0, 0, 0, 0]]
    # si le test ci-dessous échoue, vous avez un problème d'aliasing 
    $$$ g[1][1] = 1
    $$$ g
    [[0, 0, 0, 0], \
     [0, 1, 0, 0], \
     [0, 0, 0, 0]]
    """
    return [[0]*largeur for i in range(hauteur)]


def est_valide(grille:list[list[int]], ind_colonne:int) -> bool:
    """Renvoie vrai ssi l'indice `ind_colonne` est un indice valide de
    colonne de la grille `grille` et dans laquelle on peut ajouter un jeton.
    `ind_colonne` de la grille `grille`.
    Précondition : grille non vide
    $$$ g = [[1, 0, 0, 0], \
             [1, 1, 0, 0], \
             [1, 1, 1, 0]]
    $$$ est_valide(g, -1)
    False
    $$$ est_valide(g, 0)
    False
    $$$ est_valide(g, 1)
    True
    $$$ est_valide(g, 2)
    True
    $$$ est_valide(g, 3)
    True
    $$$ est_valide(g, 4)
    False
    """
    return grille[0][ind_colonne] == 0



def ligne_de_chute(grille:list[list[int]], ind_colonne:int) -> int:
    """Renvoie l'indice de la ligne dans laquelle tomberait un jeton
    inséré dans la colonne d'indice `ind_colonne` de la grille `grille`.
    Précondition : est_valide(grille, ind_colonne)
    $$$ g = [[1, 0, 0, 0], \
             [1, 1, 0, 0], \
             [1, 1, 1, 0]]
    $$$ ligne_de_chute(g, 1)
    0
    $$$ ligne_de_chute(g, 2)
    1
    $$$ ligne_de_chute(g, 3)
    2
    """
    ind_chute = -1
    Status = True
    for i in range(len(grille)):
        if grille[i][ind_colonne] == 0 and Status:
            ind_chute += 1
        else:
            Status = False
    return ind_chute

def poser_jeton(grille:list[list[int]], ind_colonne:int, joueur:int) -> int:
    """Mute la grille `grille` en inserant dans la colonne d'indice `ind_colonne`
    un jeton du joueur `joueur`, et renvoie l'indice de la ligne d'arrivée de
    ce jeton.
    Précondition : est_valide(grille, ind_colonne) et joueur in {1, 2}
    $$$ g = [[1, 0, 0, 0], \
             [1, 1, 0, 0], \
             [1, 1, 1, 0]]
    $$$ poser_jeton(g, 2, 2)
    1
    $$$ poser_jeton(g, 3, 2)
    2
    $$$ g
    [[1, 0, 0, 0], \
     [1, 1, 2, 0], \
     [1, 1, 1, 2]]
    """
    ind_chute = ligne_de_chute(grille, ind_colonne)
    grille[ind_chute][ind_colonne] = joueur
    return ind_chute



def nombre_jetons_colonne(grille:list[list[int]],
                          position:tuple[int, int],
                          joueur:int,
                          nb_max:int) -> int:
    """Renvoie le nombre de jetons de la grille `grille` :
        - en partant de `position`
        - vers le bas
        - tant que la couleur est la même que `joueur`
        - inutile de compter plus que `nb_max`
    $$$ g = [[0, 2, 2, 0], \
             [1, 2, 2, 0], \
             [2, 1, 2, 0], \
             [1, 2, 2, 2]]
    $$$ nombre_jetons_colonne(g, (0, 1), 2, 4)
    2
    $$$ nombre_jetons_colonne(g, (0, 2), 2, 4)
    4
    $$$ nombre_jetons_colonne(g, (0, 2), 2, 2)
    2
    $$$ nombre_jetons_colonne(g, (0, 2), 2, 5)
    4
    """
    ind_ligne, ind_colonne = position
    
    while i <= nb_max and 


def nombre_jetons_ligne(grille:list[list[int]],
                        position:tuple[int, int],
                        joueur:int,
                        nb_max:int) -> int:
    """Renvoie le nombre de jetons de la grille `grille` :
        - en partant de `position`
        - vers la droite puis la gauche
        - tant que la couleur est la même que `joueur`
        - inutile de compter plus que `nb_max`
    $$$ g = [[2, 0, 2, 2], \
             [1, 2, 2, 1], \
             [2, 2, 2, 2]]
    $$$ nombre_jetons_ligne(g, (2, 0), 2, 4)
    4
    $$$ nombre_jetons_ligne(g, (2, 3), 2, 4)
    4
    $$$ nombre_jetons_ligne(g, (1, 2), 2, 4)
    2
    $$$ nombre_jetons_ligne(g, (0, 3), 2, 4)
    2
    """
    ind_ligne, ind_colonne = position


def nombre_jetons_diag1(grille:list[list[int]],
                        position:tuple[int, int],
                        joueur:int,
                        nb_max:int) -> int:
    """Renvoie le nombre de jetons de la grille `grille` :
        - en partant de `position`
        - vers bas et droite puis haut et gauche
        - tant que la couleur est la même que `joueur`
        - inutile de compter plus que `nb_max`
    $$$ g = [[2, 2, 0, 0], \
             [1, 2, 2, 0], \
             [1, 1, 2, 2], \
             [1, 1, 1, 2]]
    $$$ nombre_jetons_diag1(g, (0, 0), 2, 4)
    4
    $$$ nombre_jetons_diag1(g, (3, 3), 2, 4)
    4
    $$$ nombre_jetons_diag1(g, (1, 1), 2, 4)
    4
    $$$ nombre_jetons_diag1(g, (1, 2), 2, 4)
    3
    """
    ind_ligne, ind_colonne = position

def nombre_jetons_diag2(grille:list[list[int]],
                        position:tuple[int, int],
                        joueur:int,
                        nb_max:int) -> int:
    """Renvoie le nombre de jetons de la grille `grille` :
        - en partant de `position`
        - vers bas et gauche puis haut et droite
        - tant que la couleur est la même que `joueur`
        - inutile de compter plus que `nb_max`
    $$$ g = [[0, 2, 2, 2], \
             [1, 2, 2, 1], \
             [2, 2, 1, 1], \
             [2, 1, 2, 1]]
    $$$ nombre_jetons_diag2(g, (0, 3), 2, 4)
    4
    $$$ nombre_jetons_diag2(g, (3, 0), 2, 4)
    4    
    """


