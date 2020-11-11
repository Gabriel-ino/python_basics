print('-='*20)
print(' CADASTRE UMA PESSOA ')
print('-='*20)
cont1 = cont2 = cont3 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
    if idade >= 18:
        cont1 += 1
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F' and idade < 20:
        cont3 += 1
    v = str(input('Quer continuar? ')).strip().upper()[0]
    while v not in 'SN':
        v = str(input('Quer continuar? ')).strip().upper()[0]
    if v == 'N':
        break
print(f'Foram/foi regitrada(s) {cont1} pessoa(s) maior(es) de idade, {cont2} do sexo masculino e'
      f' {cont3} mulher(es) menor(es) de 20 anos')


