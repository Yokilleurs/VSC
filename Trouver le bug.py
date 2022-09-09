def compte_bits(valeur):
    nb_bits = 1
    while valeur < 2**nb_bits:
        nb_bits = nb_bits + 1
    return nb_bits

compte_bits(16000000)
    