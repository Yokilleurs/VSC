def decimale_binaire(n):
    d = ''
    while n > 0:
        r = n%2
        n = n//2
        d = str(r) + d
    return d


def decimale_hexadecimale(n):
    d = ''
    while n > 0:
        r = n%16
        n = n//16
        if r > 9:
            DecToHex = ('A', 'B', 'C', 'D', 'E', 'F')
            r = DecToHex[r - 10]
        d = str(r) + d
    return d

def decimale_base(n, base):
    d = ''
    while n > 0:
        r = n%base
        n = n//base
        if r > 9:
            DecToHex = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'K', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            r = DecToHex[r - 10]
        elif r > 36:
            print('Base is too high')
        d = str(r) + d
    return d