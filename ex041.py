from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento do atleta: '))
idade = atual - ano

if idade <= 9:
    cat = 'Mirim'
elif 9 < idade <= 14:
    cat = 'Infantil'
elif 14 < idade <= 19:
    cat = 'Junior'
elif idade == 20:
    cat = 'Sênior'
elif idade > 20:
    cat = 'Master'

print('A categoria do atleta é {} por ter {} anos de idade.'.format(cat, idade))
