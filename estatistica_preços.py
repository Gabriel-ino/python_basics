total = cont = m = gamb = 0
barato = []
while True:
    nome = str(input('Digite o nome do produto: '))
    val = float(input('Digite o valor do produto: R$'))
    if gamb == 0:
        m = val
        barato = nome
        gamb += 1
    total += val
    if val > 1000:
        cont += 1
    if val < m:
        m = val
        barato = nome
    p = str(input('Deseja continuar? [S/N]')).strip().upper()
    while p not in 'SN':
        p = str(input('Deseja continuar? [S/N]')).strip().upper()
    if p == 'N':
        print('Obrigado pelas compras!')
        break

print(f'O produto mais barato foi {barato} e custa R${m}\nVocê comprou {cont} produtos acima de R$ 1000,00\n'
      f'O total de suas compras foi RS${total}')


