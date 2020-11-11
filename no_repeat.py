lista = []
cont = 0
while True:
    val = float(input('Digite aqui qualquer valor: '))
    if val in lista:
        cont += 1
    else:
        lista.append(val)
    x = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if x == 'N':
        break
    if x not in 'SN':
        x = str(input('Valor inválido. Deseja continuar? [S/N]'))

print(f'Os valores digitados foram:{lista}\nVocê repetiu um valor já existente {cont} vez(es)'
      f'\nValores em ordem crescente: {sorted(lista)}')

