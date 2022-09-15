def test(vf):
    if vf == "true":
        vf = 1
    elif vf == "false":
        vf = 0
    else:
        vf = "Valeur incorrecte"
    return vf