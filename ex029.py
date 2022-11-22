import time
print('\033[1;33mVruuum vruuuum')
v = int(input('\033[36mVocê está andando de carro, qual sua velocidade em Km/h?\033[m\n'))
limite = int(input('Velocidade máxima da via: '))
taxa_multa = 7
taxa = 0.1
limite2 = limite * (1+taxa)
multa = (v-limite)*taxa_multa
if v>limite2:
    print('\033[31mVocê acabou de passar por um pardal e foi multado! Você passou a {}Km/h e a velocidade máxima da via era 80Km/h'.format(v))
    print('\033[31mO valor da multa é de R${:.2f}'.format(multa))
elif v>limite:
    print('\033[33mCuidado! Você não foi multado mas está excedendo a velocidade da via\033[m')
else:
    print('\033[34mQue ótimo, você não ultrapassou a velocidade máxima da via!')
print('\033[1;33mVruuuuum')