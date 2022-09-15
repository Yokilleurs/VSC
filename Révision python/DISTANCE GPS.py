def temps_en_secondes(he, min, sec, ms ):
  secondes_finales = (he * 60 * 60)
  secondes_finales = secondes_finales + (min * 60)
  secondes_finales = secondes_finales + sec
  secondes_finales = secondes_finales + (ms / 1000)
  return secondes_finales



print(temps_en_secondes(15, 59, 59, 910), temps_en_secondes(16, 0, 0, 15))

def distance(ta, td):
  df = td - ta
  df = df * 300000
  return df

print(distance(temps_en_secondes(15,59,59,910),temps_en_secondes(16,0,0,15)))

