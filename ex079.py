lista = list()
while True:
    n = int(input('Digite um número para a lista: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado!')
    else:
        print('Número repetido não adicionado!')
    r = input('Deseja continuar? S/N ')
    if r.upper() in 'NAO':
        break
print(f'Você digitou os valores {sorted(lista)}')
