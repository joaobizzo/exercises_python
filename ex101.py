def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    vot = 0
    if idade < 16:
        return f'Com {idade} anos, o voto ainda não é permitido'
    elif 16 <= idade < 18 or idade >= 65:
        return f' Com {idade} anos, o voto é opcional'
    else:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO'


ano = int(input(f'Ano de nascimento: '))
print(voto(ano))
