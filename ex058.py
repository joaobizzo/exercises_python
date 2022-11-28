from random import randint

comp = randint(0, 10)
print('\033[34m-=-\033[m'*17)
print('\033[35mPensei em um número entre 0 e 10. Adivinhe qual é\033[m! ')
print('\033[34m-=-\033[m'*17)

c = 0
acertou = False
while not acertou:
    num = int(input('Qual seu palpite?\n'.format(comp)))
    c += 1
    if num == comp:
        acertou = True
    else:
        if num > comp:
            print('Menos.....')
        elif num < comp:
            print('Mais......')
print('Você acertou, era mesmo o número {}.\nVocê levou {} palpites para acertar.'.format(comp, c))
