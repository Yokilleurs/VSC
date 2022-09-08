def dms_a_decimale(d, d_m, d_s):
  DD = d_s / 3600
  DD = DD + d_m / 60
  DD = DD + d
  return DD

print(dms_a_decimale(12,20,42))

