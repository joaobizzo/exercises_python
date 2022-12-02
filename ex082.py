pares = list()
impares = list()
lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? S/N '))
    if r.lower() in 'nao':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
