import datetime
qtd = int(input('Digite aqui a quantidade de pessoas a serem analisadas: '))
cont1 = 0
cont2 = 0
data_atual = datetime.date.today().year
for c in range (0,qtd):
    nasc = int(input('Digite aqui o ano em que a pessoa nasceu: '))
    idade = data_atual - nasc
    if idade >= 18:
        cont1 += 1
    else:
        cont2 += 1
print('Ao todo, você digitou {} pessoas maiores de idade e {} pessoas menores de idade'.format(cont1, cont2))
