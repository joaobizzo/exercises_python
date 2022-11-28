s = input('Digite seu sexo [F/M]: ').strip().upper()
while s not in 'MmFf':
    s = input('Digite corretamente: ').upper()
print('Dados cadastrados corretamente')
