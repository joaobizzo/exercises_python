from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
jogo = {
    'jogador1' : randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}o lugar: {v[0]} com {v[1]}')
    sleep(0.5)
