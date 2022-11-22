#Jogo da adivinhação V1.0

#import random
#num = int(input('Adivinhe o número que estou pensando entre 1 e 5: '))
#s = [1, 2, 3, 4, 5]
#es = random.choice(s)
#if num == es:
#    print('Você acertou, era mesmo o número {}'.format(es))
#else:
#    print('Você errou! Era o número {}'.format(es))

from random import randint
from time import sleep
comp = randint(1,10)
print('\033[34m-=-\033[m'*17)
print('\033[35mPensei em um número entre 1 e 10. Adivinhe qual é\033[m! ')
print('\033[34m-=-\033[m'*17)
num = int(input(''))
print('Processando...')
sleep(1)
if num == comp:
    print('Você acertou, era mesmo o número {}'.format(comp))
else:
    print('Você errou! Era o número {}'.format(comp))
