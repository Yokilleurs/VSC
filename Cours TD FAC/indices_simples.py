# Exercices à savoir faire pour le DS

# Question 5

def minimum(nombres: list[int]) -> int:
    """Renvoie la plus petite valeur des éléments de `nombres`
    Précondition : `nombres` n'est pas la liste vide
    Exemple(s) :
    $$$ minimum([5, 2, 7, 3])
    2
    $$$ minimum([-5, -5, -3])
    -5
    $$$ minimum([0, 3, -1])
    -1
    """
    minima = nombres[0]
    for i in range(len(nombres)):
        if nombres[i] < minima:
            minima = nombres[i]
    return minima


# Question 6

def regroupement(l1: list[int], l2: list[int]) -> list[tuple[int, int]]:
    """Renvoie une liste contenant les couples formés par les éléments des liste `l1` et `l2` partageant le même indice.
    Précondition : aucune
    Exemple(s) :
    $$$ regroupement([1, 2, 3], [4, 5, 6])
    [(1, 4), (2, 5), (3, 6)]
    $$$ regroupement([1, 2, 3, 4], [4, 5, 6])
    [(1, 4), (2, 5), (3, 6)]
    $$$ regroupement([], [4, 5, 6])
    []
    """
    return [(l1[i],l2[i]) for i in range(minimum([len(l1),len(l2)]))]
    

# Question 7

def moyenne(notes: list[float], coefficients: list[int]) -> float:
    """renvoie la moyenne de ces notes coefficientées par ces coefficients.
    Précondition : - les deux listes sont de même longueur
                   - la somme des coefficients est strictement positive
    Exemple : Pour calculer la moyenne de 10 coef 1, 10 coef 2 et 20 coef 3, on calcule
    (10 × 1 + 10 × 2 + 20 × 3) / (1 + 2 + 3) = 15
    $$$ moyenne([10.0, 10.0, 20.0], [1, 2, 3])
    15.0
    """
    somme_notes_decoeff = 0
    for i in range(len(notes)):
        somme_notes_decoeff += notes[i]*coefficients[i]
    sommes_coefs = 0
    for i in range(len(coefficients)):
        sommes_coefs += coefficients[i]
    return somme_notes_decoeff/sommes_coefs

# Question 8

def miroir(chaine: str) -> str:
    """Renvoie les caractères de `chaine` dans l’ordre inverse.
    Précondition : /
    Exemple(s) :
    $$$ miroir("informatique")
    'euqitamrofni'
    $$$ miroir("")
    ''
    """
    return chaine[::-1]

# Question 9

def jointure(chaines_a_joindre: list[str], separateur: str) -> str:
    """Renvoie une chaîne qui intercale separateur entre chaque élément de chaines_a_joindre.
    Précondition : chaines_a_joindre est non vide
    Exemple(s) :
    $$$ jointure(["23", "10", "2024"], '/')
    '23/10/2024'
    $$$ jointure(["tout seul"], '*')
    'tout seul'
    """
    joint = ''
    for i in range(len(chaines_a_joindre)):
        joint += chaines_a_joindre[i]+separateur
    return joint[:len(joint)-len(separateur)]

# Les questions suivantes sont plus difficiles, mais ce serait mieux que vous arriviez à les refaire pour le DSi

# Question 10

def argminima(liste: list[int]) -> list[int]:
    """renvoyant la liste des indices d’occurrences du plus petit élément de liste.
    Précondition : liste est non vide
    Exemples :
    Dans ce premier exemple, le plus petit élément est 3, qui se trouve à l'indice 1
    $$$ argminima([4, 3, 7])
    [1]
    Dans ce deuxième exemple, le plus petit élément est 0, qui se trouve à la fois aux indices 0 et 1
    $$$ argminima([0, 0, 7])
    [0, 1]
    Dans ce troisième exemple, le plus petit élément est 1, qui se trouve aux indices 1 et 3
    $$$ argminima([2, 1, 3, 1])
    [1, 3]
    """
    minima = minimum(liste)
    index_list = []
    for i in range(len(liste)):
        if liste[i] == minima:
            index_list.append(i)
    return index_list
    

# Question 11

def suffixes(chaine: str) -> list[str]:
    """Renvoie la liste de tous les suffixes de `chaine`.
    '' et chaine sont deux suffixes triviaux de chaines.
    Précondition : /
    Exemple(s) : 
    $$$ suffixes('fin')
    ['fin', 'in', 'n', '']
    $$$ suffixes('')
    ['']
    """
    return [chaine[i:] for i in range(len(chaine)+1)]

def decoupage_simple(string):
    temp = ''
    final = []
    for i in range(len(string)):
        if string[i] == '+' or string[i] == '-':
            final.append(temp)
            final.append(string[i])
            temp = ''
        else:
            temp += string[i]
    if temp != '':
        final.append(temp)
    return final

def calcul(liste):
    if liste[1] == '+':
        return int(liste[0]) + int(liste[2])
    elif liste[1] == '-':
        return int(liste[0]) - int(liste[2])

def evaluation(liste):
    return calcul(decoupage_simple(liste))

def distribution(string):
    final_indice_pair = []
    final_indice_impair = []
    for i in range(len(string)):
        if i % 2 == 0:
            final_indice_pair.append(string[i])
        elif i % 2 == 1:
            final_indice_impair.append(string[i])
    return (final_indice_pair, final_indice_impair)

def entiers(liste):
    return [int(liste[i]) for i in range(len(liste))]

def reduction(nombres, operateurs):
    last_num = nombres[0]
    for i in range(len(operateurs)):
        if operateurs[i] == '+':
            last_num += nombres[i+1]
        elif operateurs[i] == '-':
            last_num -= nombres[i+1]
    return last_num

def calculatrice(expression):
    nombres_string, operateurs = distribution(expression)
    nombres = entiers(nombres_string)
    return reduction(nombres, operateurs)
    return reduction(entiers(distribution(expression)[0]), distribution(expression)[1])