dados = dict()
dados['nome'] = str(input('Nome do aluno: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['result'] = str('Aprovado')
elif 5 <= dados['media'] < 7:
    dados['result'] = str('Recuperação')
else:
    dados['result'] = str('Reprovado')
print('-=' * 15)
print(f'Nome = {dados["nome"]}')
print(f'Média = {dados["media"]}')
print(f'Situação final = {dados["result"]}')
