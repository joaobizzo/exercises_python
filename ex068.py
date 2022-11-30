from random import randint
v = 0
print('-='*10)
print('Par ou ímpar')
print('-='*10)
while True:
    jog = int(input('Seu número: '))
    comp = randint(0, 10)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador jogou {comp} a soma deu {total}')
    print('DEU PAR')  if total % 2 == 0 else print('DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[34mVocê VENCEU!\033[m')
            v += 1
        else:
            print('\033[34mVocê PERDEU\033[m')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('\033[34mVocê VENCEU!\033[m')
            v += 1
        else:
            print('\033[34mVocê PERDEU\033[m')
            break
    print('Vamos jogar novamente...')
print('=='*9)
print('\033[31mGAME OVER\033[m')
print('=='*9)
print(f'Você acertou {v} tentativas seguidas!')
