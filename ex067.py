c = t = n = 0
n = int(input('Digite um número para tabuada:'))
while True:
    if n < 0:
        break
    if c < 10:
        c += 1
        print(f'{n} X {c} = {n * c}')
    else:
        print('-' * 15)
        n = int(input('Digite um número para tabuada:'))
        print('-' * 15)
        c = 0
print('Tabuada encerrada')
