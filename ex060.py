from time import sleep
n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando \033[32m{}!\033[36m'.format(n))
sleep(0.8)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
