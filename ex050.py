s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont +=1
print('Você informou {} números PARES e a soma entre eles é {}'.format(cont, s))
