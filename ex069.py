r = 's'
conth = 0
contm = 0
conti = 0
while r in 'Ss':
    print('CADASTRE UMA PESSOA:')
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').upper().strip()[0]
    print('-'*19)
    r = input('Deseja continuar?').strip()[0]
    print('-' * 19)
    if s == 'M':
        conth +=1
    if s == 'F' and i < 20:
        contm += 1
    if i < 18:
        conti += 1
print(f'{conti} pessoas têm menos de 18 anos\n{conth} são homens\n{contm} mulheres tem menos de 20 anos')
