from time import sleep
n = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while n != 5:
    print('-=-'*9)
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    n = int(input('Qual sua opção? '))
    print('-=-' * 9)
    if n == 1:
        print('\033[31mA soma entre {} e {} é {}\033[m'.format(n1, n2, n1 + n2))
    elif n == 2:
        print('\033[31mO produto entre {} e {} é {}\033[m'.format(n1, n2, n1 * n2))
    elif n == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif n == 4:
        print('\033[33mNovos números:\033[m')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif n == 5:
        print('Finalizando...')
    sleep(2)
sleep(0.8)
print('Programa encerrado')