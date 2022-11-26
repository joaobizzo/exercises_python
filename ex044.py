valor = float(input('Preço das compras: R$'))
esc = int(input("""
Escolha a forma de pagamento de digite o número:
(1) À vista dinheiro/cheque/débito - 10% de desconto
(2) À vista no cartão - 5% de desconto
(3) Em até 2x no cartão - preço normal
(4) 3x ou mais - 20% de juros
"""))
if esc == 1:
    preço = valor * 0.9
elif esc == 2:
    preço = valor * 0.95
elif esc == 3:
    preço = valor
    print('2x de {}'.format(preço/2))
elif esc == 4:
    parcela  = int(input('Quantas parcelas? '))
    preço = valor * 1.2
    print('3x de {:.2f}'.format(preço/parcela))
print('Sua compra de {:.2f} vai custar o total de R${:.2f}'.format(valor, preço))
