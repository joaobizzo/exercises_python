numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[n]}')
