brasileirao = ('América', 'Athletico', 'Atlético-GO',' Atlético-MG', 'Bahia'
               , 'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo')
print(f'Os cinco primeiros colocados são:{(brasileirao[0:5])}')
print(f'Os quatro ultimos colocados são: {(brasileirao[-4:])}')
print(f'Em lista alfabética: {(sorted(brasileirao))}')
print(f'O chapecoense está em {brasileirao.index("Chapecoense")+1}º')

