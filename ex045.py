import random
import time

#jokempô 1.0
print('='*13)
print('Jokempô v1.0')
print('='*13)

lista = ['Pedra', 'Papel', 'Tesoura']
comp = random.randint(0,2)
print("""Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura""")
jog = int(input('Qual sua jogada? '))
print('JO')
time.sleep(0.7)
print('KEN')
time.sleep(0.7)
print('PO!')
time.sleep(0.7)
print('='*35)
print('Computador jogou {}'.format(lista[comp]))
if comp == 0: #computador pedra
    if jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE')
    elif jog == 3:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')
elif comp == 1: #computador papel
    if jog == 1:
        print('COMPUTADOR VENCE')
    elif jog == 2:
        print('EMPATE!')
    elif jog == 3:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida')
elif  comp == 2: #computador tesoura
    if jog == 1:
        print('JOGADOR VENCE')
    elif jog == 2:
        print('COMPUTADOR VENCE')
    elif jog == 3:
        print('EMPATE')
    else:
        print('Jogada inválida')
print('='*35)
