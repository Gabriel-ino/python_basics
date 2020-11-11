ini = int(input('Digite aqui o valor inicial: '))
raz = int(input('Digite aqui a razão: '))
decimo = ini + (10-1) * raz

while ini < decimo + raz:
    print('{}'.format(ini), end='->')
    ini += raz

add = str(input(' Você quer adicionar mais termos?')).strip().upper()[0]
if add == 'S':
    ag = int(input('Quantos termos você quer mostrar a mais?'))
    cont = 0
    while cont < ag:
        print('{}'.format(ini), end='->')
        ini += raz
        cont += 1
print('FIM!')
