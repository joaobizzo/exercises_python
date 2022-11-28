#FIBONACCI
ant = 0
pro = 1
cont = 0
t = int(input('Termos: '))
while cont < t:
    cont += 1
    pro += ant
    ant = pro - ant
    print(pro, end=' - ')
print('fim')
