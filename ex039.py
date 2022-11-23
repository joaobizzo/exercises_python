ano = int(input('Qual o seu ano de nascimento? '))
idade = 2021 - ano

#concluir, mostrando quando o menor vai se alistar
if idade < 18:
    saldo = 18 - idade
    print('Falta {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será no ano {}'.format(ano+18))
elif idade > 18:
    saldo = idade - 18
    print('Você ja se alistou faz {} anos'.format(saldo))
    print('Você se alistou no ano {}'.format(ano+18))
else:
    print('Esse é o ano do seu alistamento!')
