#tabuada 2.0
n = int(input('Digite um número de 0 a 10: '))
print('-'*12)
for c in range(1, 11):
    print('{} x {}  = {}'.format(n, c, c*n))
print('-'*12)
