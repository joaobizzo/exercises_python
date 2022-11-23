salario = int(input('Salário: '))
if salario >1250:
    novo = salario * 1.1
else:
    novo = salario * 1.15
print('O salário recebeu um aumento de R${:.2f} ficando R${:.2f}'.format(novo-salario, novo))
