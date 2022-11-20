l = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
a2 = (l * a)
lt = a2/2
print('Para pintar uma parede de {:.1f} metros quadrados, é necessário {:.2f} litros de tinta'.format(a2,lt))