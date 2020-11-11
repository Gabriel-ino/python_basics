lista1 = []
lista2 = []
lista3 = []
while True:
    x = int(input('Digite aqui qualquer valor inteiro: '))
    lista1.append(x)
    if x % 2 == 0:
        lista2.append(x)
    else:
        lista3.append(x)
    esc = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Valor inválido. Deseja continuar? [S/N]')).strip().upper()[0]
    if esc == 'N':
        break
print(f'Lista completa: {lista1}\nLista com valores pares: {lista2}\nLista com valores ímpares: {lista3}')