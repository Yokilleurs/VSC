def compte_bits(valeur):
    nb_bits = 1
    while valeur > 2**nb_bits:
        nb_bits = nb_bits + 1
    return nb_bits

def qbits_vers_bits(valeur):
    nb_bits = 2**valeur
    return nb_bits
