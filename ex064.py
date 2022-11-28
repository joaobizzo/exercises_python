n = 0
cont = 0
soma = 0
print('\033[33m[999] para encerrar\033[m')
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
print('Você digitou {} números e a soma entre ele foi {}'.format(cont, soma-999))
