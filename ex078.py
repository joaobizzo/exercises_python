lista1 = list()
# for cont in range(0, 5):
#     lista1.append(int(input(f'Digite um valor para a posição {cont+1}: ')))
# lista2 = lista1[:]
# lista1.sort()
# print(f'O maior valor foi o {lista1[4]} na posição {lista2.index(lista1[4])+1}')
# print(f'O menor valor foi o {lista1[0]} na posição {lista2.index(lista1[0])+1}')
# print(lista2)

mai = 0
men = 0
for cont in range(0, 5):
    lista1.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        mai = men = lista1[cont]
    else:
        if lista1[cont] > mai:
            lista1[cont] = mai
        elif lista1[cont] < men:
            lista1[cont] = men
print(f'Você digitou os valores: {lista1}')
for i, v in enumerate(lista1):
    if v == mai:
        print(f'{i}...')
