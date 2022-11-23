#analisando triangulo V1.0
print('-=-'*15)
print('Analisador de triângulos V1.0')
print('-=-'*15)
print('Digite 3 retas, descobrirei se pode formar um triangulo com elas')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1< r2+r3 and r2< r1+r3 and r3<r1+r2:
    print('Pode se formar um triangulo!')
else:
    print('Não se pode formar um triangulo!')
