qtd = int(input('Digite a quantidade de pessoas a serem analisadas: '))
media = 0
velho = 0
nome2 = []
cont_2 = 0
for c in range(0, qtd):
    idade = int(input('Digite a idade da pessoa: '))
    nome = str(input('Digite o nome da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: '))
    media += idade / qtd
    if sexo == 'M' and idade > velho:
        velho = idade
        nome2 = nome
    if sexo == 'F' and idade < 20:
        cont_2 += 1

print('A média das idades é: {:.2f}\nO nome do homem mais velho é: {} e ele tem {} anos\nTêm {} mulheres abaixo de 20 anos.'.format(media, nome2, velho, cont_2 ))




