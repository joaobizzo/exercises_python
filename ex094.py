pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input(f'Sexo de {pessoa["nome"]}: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! DIGITE APENAS M/F')
    pessoa['idade'] = int(input(f'Idade de {pessoa["nome"]}: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N]')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! DIGITE APENAS S/N')
    if r == 'N':
        break
print('-=' * 20) #analise dos dados vvvv
print(f'A) Ao todo {len(galera)} pessoas foram cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão com a idade acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
