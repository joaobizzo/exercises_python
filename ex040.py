n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2)/2
print('A média do aluno é {}'.format(media))
if media < 5.0:
    print('\033[31mREPROVADO\033[m')
elif 5.0 < media <6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
elif media >= 7.0:
    print('\033[32mAPROVADO\033[m')
