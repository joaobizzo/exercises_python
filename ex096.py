def area(c, l):
    a = c * l
    print(f'A área de um terreno de {l} x {c} é de {a}m quadrados.')


print(' Controle de Terrenos')
print('-')
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
area(c, l)
