n = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite outro número: ')))
print(f'Você digitoou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro valor 3 apareceu na {n.index(3)+1}º posição')
else:
    print('O número 3 nçao apareceu nenhuma vez')
print(f'Os valores pares digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
