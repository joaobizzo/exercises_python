palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'COMPUTADOR', 'ESTUDAR', 'CURSO')
for p in palavras:
    print(f'\nNa palavra {p}: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
