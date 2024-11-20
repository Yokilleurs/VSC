def pliage(epaisseur, hauteur_objectif):
    nb_pliages = 0
    while epaisseur <= hauteur_objectif:
        epaisseur *= 2
        nb_pliages += 1
    return nb_pliages

print(f" Il faut {pliage(0.32*10**-3, 312)} pliages pour atteindre la hauteur de la tour Eiffel avec un papier d'épaisseur 0.32 mm")

def interets_cumules(capital, interets, annees=1):
    for i in range(annees):
        capital = capital * interets
    return capital

print(f"Il aura {interets_cumules(1, 1.0225, 50)} après son placement de 50 ans")

def capital_depasse(capital, interets, objectif):
    capital = interets_cumules(capital, interets)
    annees = 1
    while capital <= objectif:
        capital = interets_cumules(capital, interets)
        annees += 1
    return annees

print(f"Il lui faudra {capital_depasse(0.93, 1.0225, 4000000000)} ans pour atteindre son objectif")

