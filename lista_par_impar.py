lista = [[], []]
while True:
    x = int(input('Digite aqui um valor inteiro qualquer: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
    esc = str(input('Quer continuar? [S/N]')).strip().upper()
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]')).strip().upper()
    if esc == 'N':
        break
print(f'Números pares: {sorted(lista[0])}\nNúmeros ímpares: {sorted(lista[1])}')
