#!/usr/bin/env python3

VACHE = "        \\   ^__^\n         \\  (oo)\\_______\n            (__)\\       )\\/\\\n                ||----w |\n                ||     ||"

# Question 2

def bulle(texte: str) -> str:
    """une chaîne dont l’affichage produit un encadrement de texte
       comme illustré dans l’exemple-ci dessous.
       >>> print(bulle("bonjour"))
        _________ 
       /         \
       | bonjour |
       \_________/
    Précondition: - `texte` contient moins de 75 caractères
                  - tous les caractères de `texte` sont imprimables
    $$$ bulle("bonjour")
    '  _________ \\n/         \\\\\\n| bonjour |\\n\\\\_________/'
    """
    return (f" {'_'*(len(texte)+2)} \n/{' '*(len(texte)+2)}\\\n| {texte} |\n\{'_'*(len(texte)+2)}/")


# Question 3

def meugler(texte: str):
    """Affiche `texte` dans une bulle prononcée par la vache.
    >>> meugler("Bravo ! Continuez !")
     _____________________ 
    /                     \
    | Bravo ! Continuez ! |
    \_____________________/
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    
    Précondition: - `texte` contient moins de 75 caractères
                  - tous les caractères de `texte` sont imprimables
    """
    return f"{bulle(texte)}\n{VACHE}"

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        texte = 'rien'
    else:
        (_, texte) = sys.argv
    meugler(texte)
