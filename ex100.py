from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
