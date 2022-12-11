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
    if type(n)!=type(base)!=int:
        return "n and base must be an integer"
    elif base < 2 or n < 0:
        return "Base can't be inferior than 2 and n must be a positive integer"
    while n > 0:
        r = n%base
        n = n//base
        if r > 9:
            DecToHex = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'K', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            try: 
                r = DecToHex[r - 10]
            except IndexError as err:
                return f"Erreur : {err}. Rest is too high for base {base}"
        elif r > 36:
            print("Base is too high")
        d = str(r) + d
    return d