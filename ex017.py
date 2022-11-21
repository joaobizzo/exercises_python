import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))
h = math.hypot(co,ca)
print ('A hipotenusa é {}'.format(h))