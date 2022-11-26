#analisando triangulo V2.0
#cores
cores = {'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'vermelho' : '\033[31m',
         'ciano' : '\033[36m',
         'roxo' : '\033[35m',
         'verde': '\033[32m',
         'limpa' : '\033[m'}
#intro
print('{}-=-{}'.format(cores['roxo'], cores['limpa'])*15)
print('{}Analisador de triângulos V2.0{}'.format(cores['ciano'], cores['limpa']))
print('{}-=-{}'.format(cores['roxo'], cores['limpa'])*15)
print('Digite 3 retas, descobrirei se pode formar um triangulo com elas')


r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1< r2+r3 and r2< r1+r3 and r3<r1+r2:
    print('Pode se formar um triangulo!', end=' ')
    if  r1 == r2 == r3:
        print('Equilátero')
    elif r2 == r3 or r1 == r2 or r1 == r3:
        print('Isósceles')
    else:
       print('Escaleno')
else:
    print('Não se pode formar um triangulo!')
