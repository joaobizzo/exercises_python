from datetime import date
menores = 0
maiores = 0
ano = date.today().year
for c in range(1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu?  '.format(c)))
    i = ano-n
    if i >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são de maior\n{} pessoas são de menor'.format(maiores, menores))
