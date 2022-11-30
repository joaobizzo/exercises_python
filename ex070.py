soma = mmil = menor = cont = 0
nmenor = ''
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço do produto: R$'))
    cont += 1
    soma += p
    r = ' '
    if p > 1000:
        mmil += 1
    if cont == 1:
        menor = p
        nmenor = n
    else:
        if p < menor:
            menor = p
            nmenor = n
    while r not in 'SN':
        r = str(input('Deseja continuar?')).strip().upper()[0]
    if r == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total gasto: R${soma:.2f}')
print(f'{mmil} produtos custam mais de  R$1000.00')
print(f'O produto mais barato é o {nmenor} custando R${menor:.2f}')
