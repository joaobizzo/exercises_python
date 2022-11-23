#definindo cores
cores = {'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'vermelho' : '\033[31m',
         'ciano' : '\033[36m',
         'roxo' : '\033[35m',
         'verde': '\033[32m',
         'limpa' : '\033[m'}

#introdução
print('{}-=-{}'.format(cores['roxo'], cores['limpa'])*19)
print('{}Pedido de empréstimo bancário para aquisição de casa v1.0{}'.format(cores['ciano'], cores['limpa']))
print('{}-=-{}'.format(cores['roxo'], cores['limpa'])*19)

#variaveis
casa = int(input('Qual o valor da sua casa?: '))
salario = int(input('Qual o seu salário mensal?: '))
ano = int(input('Em quantos anos você planeja pagar?: '))
prest = casa/(ano*12)
taxa = 0.3 * salario
mes = 12*ano

#condições
if prest < taxa:
    print('{}Seu empréstimo foi aceito!\n Você deverá pagar o valor de R${:.2f} por mês, durante {} meses ({} anos).{}'.format(cores['verde'],prest, mes, ano, cores['limpa']))
elif prest == taxa:
    print('{}Seu empréstimo foi aceito por pouco, tenha cuidado com sua vida financeira.\n  Você deverá pagar o valor de R${:.2f} por mês, durante {} meses ({} anos).{}'.format(cores['amarelo'], prest, mes, ano,cores['limpa']))
else:
    print('{}Seu pedido de empréstimo foi negado :( . Você não se aplica nos requisitos, desculpe.{}'.format(cores['vermelho'], cores['limpa']))