import math
a = float(input('Ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Seno {:.2f} \n cos {:.2f} \n tan {:.2f}'.format(s,c,t))