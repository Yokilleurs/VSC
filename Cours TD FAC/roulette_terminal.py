# Fonctions de saisies et procédures d'affichage de la roulette

def afficher_invite() -> None:
    """Affiche un message d'accueil demandant de saisir un nom
    Précondition : /
    """
    print('Vous allez jouer à la roulette.')

def saisie_nom() -> str:
    """Renvoie la saisie du nom de l'utilisateur
    Précondition : /
    """
    print('Votre nom :')
    nom = input()
    return nom

def afficher_continue(nom: str, reste: int) -> None:
    """Affiche un message demandant au joueur dont le nom est `nom`
    et possédant `reste` jetons s’il veut continuer.
    Précondition : reste >= 0
    """
    print(f"Le joueur {nom} ayant {reste} souhaite t-il continuer à jouer ?")

def saisie_continue():
    
    """Attend la saisie d’une réponse de type oui/non/o/n/O/N
    et renvoie Vrai si l’utilisateur a indiqué vouloir continuer et Faux sinon.
    Précondition : /
    """
    reponse = input()
    if reponse in ['oui', 'o', 'O'] :
        return True
    if reponse in ['non', 'n', 'N']:
        return False
    else:
        print("Veuillez choisir parmis 'oui', 'non', 'o', 'n', 'O', 'N'.")

def afficher_mise(nom: str, reste: int) -> None:
    """Affiche un message demandant au joueur dont le nom est `nom`
    et possédant `reste` jetons combien il veut miser.
    Précondition : reste > 0
    """
    print('Saisissez une mise')

def saisie_mise(reste: int) -> int:
    """Attend la saisie d’une mise et renvoie l'entier représenté par la valeur
    saisie.
    Précondition : reste > 0
    """
    return int(input())

def afficher_pari(nom: str, reste: int, mise: int) -> None:
    """Affiche un message demandant au joueur dont le nom est `nom`
    et possédant `reste` jetons sur quoi il veut parier `mise` jetons.
    Précondition : reste >= 0, mise > 0
    """
    print("Choisisez un pari (exemples : rouge, impaire, 14, passe, ...)")

# À décommenter pour la partie facultative
from roulette import pari_valide

def saisie_pari(reste: int) -> str:
    """Attend la saisie d’un pari et renvoie ce pari.
    Précondition : reste >= 0
    """
    return str(input())

def afficher_case(nom: str, case: int) -> None:
    """Affiche un message indiquant au joueur dont le nom est `nom`
    que la bille est tombée sur la case `case`.
    Précondition : 0 <= case <= 36
    """
    print(f"La bille est tombée sur {case} pour {nom}")

def afficher_gains(nom: str, gagne: bool, gains: int) -> None:
    """Affiche un message indiquant au joueur dont le nom est `nom`
    si il a gagné ou non (`gagne`) et combien (`gains`).
    Précondition : si gagne est vrai, gains > 0 sinon gains = 0
    """
    if gagne == True: 
        print(f"Le joueur {nom} a gagné {gains} jetons lors de ce pari.")
    elif gagne == False:
        print(f"Le joueur {nom} n'a pas gagné.")

def afficher_reste(nom: str, reste: int) -> None:
    """Affiche un message indiquant au joueur dont le nom est `nom`
    et possédant `reste` jetons combien il lui reste de jetons.
    Précondition : reste > 0
    """
    print(f"Le joueur {nom} a {reste} jetons.")
