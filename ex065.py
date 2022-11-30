maior = menor = cont = soma = r = 0
while r != 'N':
    n = int(input('Digite um número: '))
    r = input('\033[34mDeseja continuar? \033[35m[S/N]\033[m').upper().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont
print('Você digitou {} números, a soma deles é {}, a média {:.2f}, o maior número foi o {} e o menor foi {}'.format(cont, soma, media, maior, menor))