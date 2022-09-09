from math import degrees
from numbers import Integral


def dms_a_decimale(d, d_m, d_s):
  decim = d_s / 3600
  decim = decim + d_m / 60
  decim = decim + d
  return decim

print(dms_a_decimale(12,20,42))

def decimale_a_dms(decimale):
  deg = int(decimale) # avoir l'entier (correspond au °)
  reste = (decimale - deg) 
  minutes = int(reste * 60)
  reste = reste * 60 - minutes
  secondes = int(reste*60)
  return deg, minutes, secondes

