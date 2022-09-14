def mails(nombre, t, n):
    for i in range(n):
        nombre = nombre * (1 + t /100) + nombre # ajout de + nombre qui permet de calculer le nombre d'e-mails reçu en tout pendant n années avec un taux d'augmentation de t%
    return nombre