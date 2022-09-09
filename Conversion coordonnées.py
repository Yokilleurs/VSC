from math import degrees
from numbers import Integral


def dms_a_decimale(d, d_m, d_s):
  decim = d_s / 3600
  decim = decim + d_m / 60
  decim = decim + d
  return decim

print(dms_a_decimale(12,20,42))

def decimale_a_dms(decimale):
  degres = int(decimale) # avoir l'entier (correspond au °)
  decim = (decimale - degres) # donne à decim la valeur des décimales restantes
  
  return degres, minutes, secondes

print(decimale_a_dms(12.345))