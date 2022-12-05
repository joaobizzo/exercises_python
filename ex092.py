from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contrat'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: '))
    dados['aposent'] = dados['idade'] + (dados['contrat'] + 35 - datetime.now().year)
else:
    print('Não possui Carteira de Trabalho')
print(dados)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
