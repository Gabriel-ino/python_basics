lista = []
lista1 = []
cont = 0
while True:
    nome = str(input('Digite aqui o nome do(a) aluno(a): '))
    lista.append(nome)
    n1 = float(input('Digite aqui a primeira nota do(a) aluno(a): '))
    lista.append(n1)
    n2 = float(input('Digite aqui a segunda nota do(a) aluno(a): '))
    lista.append(n2)
    media = (2*n1 + 3*n2)/5
    lista.append(media)
    lista1.append(lista[:])
    lista.clear()
    cont += 1
    esc = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Valor inválido. Quer continuar [S/N]?')).strip().upper()[0]
    if esc == 'N':
        break

print('num', end='          ')
print('nome', end='           ')
print('média')
print('-='*20)
for c in range (0, cont):
    print('', c, end='     ')
    print(lista1[c][0], end='    ')
    if c == cont - 1:
        print('   ', f'{lista1[c][3]:.2f}')
        break
    print('   ', lista1[c][3])
print('-='*20)
esc1 = str(input('Você quer verificar as notas dos alunos [S/N]? ')).strip().upper()[0]
while esc1 not in 'SN':
    esc1 = str(input('Você quer verificar as notas dos alunos [S/N]?')).strip().upper()[0]
if esc1 == 'S':
    print('num', end='         ')
    print('nome', end='           ')
    print('n1', end='      ')
    print('n2')
    for x in range (0, cont):
        print('', x, end='     ')
        print(lista1[x][0], end='     ')
        if x == cont - 1:
            print('  ',f'{lista1[x][1]:.2f}', end='     ')
            print('  ', f'{lista1[x][2]:.2f}')
            break
        print(lista1[x][1], end='    ')
        print(lista1[x][2])
