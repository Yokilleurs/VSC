import roulette
import roulette_terminal

def introduction():
    roulette_terminal.afficher_invite()
    nom = roulette_terminal.saisie_nom()
    reste = roulette_terminal.saisie_reste()
    return (nom, reste)

(nom, reste) = introduction()

def partie(reste:int=reste, nom:str = nom):
    roulette_terminal.afficher_mise(nom, reste)
    mise = roulette_terminal.saisie_mise(reste)

    roulette_terminal.afficher_pari(nom,reste,mise)
    pari = roulette_terminal.saisie_pari(reste)

    case = roulette.tirage_roulette()
    reste = reste - mise
    print(f"Vous avez misé {mise}. Il vous reste donc {reste}.")
