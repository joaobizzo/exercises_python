#nao sei o que é isso
n1 = int(input('Digite um número inteiro: '))
n = int(input('Escolha qual será a base de conversão:\n[ 1 ] para binário; \n[ 2 ] para octal; \n[ 3 ] para hexadecimal; \n'))
if n == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif n == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif n == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, hex(n1)[:2]))
else:
    print('Opção inválida')
