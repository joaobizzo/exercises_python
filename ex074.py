from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os números: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior número sorteado foi o {max(num)}')
print(f'O menor número sorteado foi o {min(num)}')
