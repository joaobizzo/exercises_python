print('-='*20)
print('{:^40}'.format('BANCO JONHIS'))
print('-='*20)

num = int(input('Digite o valor que você deseja sacar: R$'))
total = num
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de cédulas de {totced} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-='*20)
print('{:^40}'.format('PROGRAMA CAIXA ELETRONICO ENCERRADO'))
print('-='*20)
