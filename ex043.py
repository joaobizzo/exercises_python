peso = float(input('Qual o seu peso em kilos? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso/(altura**2)

if imc <= 18.5:
    taxa = '\033[33mAbaixo da média\033[m'
elif 18.5 < imc <= 25:
    taxa = '\033[36mPeso ideal\033[m'
elif 25 < imc <= 30:
    taxa = '\033[33mSobrepeso\033[m'
elif 30 < imc <= 40:
    taxa = '\033[31mObesidade\033[m'
elif imc > 40:
    taxa = '\033[31mObesidade mórbida\033[m'

print('Com o {}Kg e {}m o IMC é {:.2f} e é classificado como {}'.format(peso, altura, imc, taxa))
