lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Deseja continuar? S/N ')
    if r.lower() in 'nao':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem crescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista')
