p = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
dez = p + (10-1) * r
for c in range(p, dez + r, r):
    print(c, end=' -> ')
print('fim')



#V  2
#cont = 0
#print(p, end='->')
#for c in range(1, 10):
#    cont += 1
#    pt = p + (cont * r)
#    print(pt, end=' -> ')