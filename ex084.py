dados = list()
lista = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    r = str(input('Deseja continuar? [S/N]'))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    if r in 'Nn':
        break

print(f'Ao todo, {len(lista)} pessoas foram cadastradas')
print(f'O maior peso foi de {mai}Kg.Peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {men}Kg. Peso de {men}', end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
