#GERADOR PA 2.0
cont = 0
print('\033[36mGerador de PA\033[m')
print('\033[31m-=\033[m'*12)
p = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
t = int(input('Quantos termos? '))
while cont < t:
    cont += 1
    p += r
    print(p, end=' -> ')
print('Fim')
