d = int(input('Distância da viagem em Km: '))
#preço = d * 0.5 if d <=200 else preço = d * 0.45
if d <= 200:
    preço = d * 0.5
else:
    preço = d * 0.45
print('O preço da passagem é R${:.2f}'.format(preço))
