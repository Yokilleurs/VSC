

def promotion(prix_initial):
    if prix_initial <= 100:
        prix_final = prix_initial * 0.90 + 10
    elif prix_initial >= 150:
        prix_final = prix_initial * 0.80
    else:
        prix_final = prix_initial * 0.80 + 10
    return prix_final

