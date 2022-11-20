km = float(input('Quantos km rodados? '))
d = int(input('Quantos dias ele foi alugado? '))
pkm = km*0.15
pd = d*60
t = pkm + pd
print('O valor total foi de R${:.2f}'.format(t))