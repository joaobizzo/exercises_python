somaidade = 0
somam = 0
maisv = 0
nomev = ''
for c in range(1, 5):
    print('-----{}ª PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if sexo in 'Ff' and idade < 20:
        somam += 1
    if sexo in 'Mm':
        if c == 1:
            maisv = idade
            nomev = nome
        else:
            if idade > maisv:
                maisv = idade
                nomev = nome

media = somaidade / 4
print('A média das idades é de {}'.format(media))
print('Nessa lista, {} mulheres tem menos de 20 anos'.format(somam))
print('O {} é o homem mais velho com {} anos '.format(nomev, maisv))
