n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro valor ({}) é o maior'.format(n1))
elif n2 > n1:
    print('O segundo valor ({}) é o maior'.format(n2))
else:
    print('Os dois valores são iguais')
