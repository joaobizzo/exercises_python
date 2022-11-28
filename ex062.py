#GERADOR PA 3.0
cont = 0
print('\033[36mGerador de PA\033[m')
print('\033[31m-=\033[m'*12)
p = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
t = 10

while t != 0:
    cont += 1
    p += r
    print(p, end=' -> ')
    t -= 1
    if t == 0:
        t = int(input('Quantos termos a mais? '))
print('Fim')
