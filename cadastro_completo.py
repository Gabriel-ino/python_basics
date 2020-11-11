#Programa para cadastro de pessoas, indicando as mulheres, pessoas com idade maior que a média das idades e
#

lista = {}
lista1 = []
listaf = []
listamm = []
cont = soma_idade = 0
while True:
    lista.clear()
    lista['nome'] = str(input('Digite aqui o nome da pessoa: '))
    idade = int(input('Digite aqui a idade da pessoa: '))
    lista['idade'] = idade
    soma_idade += idade
    lista['sexo'] = str(input('Digite aqui o sexo da pessoa [M/F]: ')).strip().upper()[0]
    while lista['sexo'] not in 'MF':
        lista['sexo'] = str(input('Valor inválido. Digite aqui o sexo da pessoa [M/F]: ')).strip().upper()[0]
    lista1.append(lista.copy())
    if lista['sexo'] == 'F':
        listaf.append(lista['nome'])
    cont += 1
    esc = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Valor inválido. Quer continuar [S/N]?')).strip().upper()[0]
    if esc == 'N':
        break
media = soma_idade / cont
if not listaf:
    listaf = str('nenhuma mulher foi cadastrada!')
print(f'Foram cadastradas {cont} pessoas\nA média de idade é {media:.2f}\nAs mulheres são:{listaf}\n'
      f'As pessoas com idade acima da média são: ')
for p in lista1:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'  {k} = {v}\n')




