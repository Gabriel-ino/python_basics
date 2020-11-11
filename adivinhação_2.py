from numpy import random
num = random.randint(0, 10)
ad = int(input('Pensei em um número, tente adivinhar qual é, ele está entre 0 e 10 e é inteiro: '))
cont = 1
while ad != num:
    ad = int(input('Número errado, tente novamente: '))
    cont += 1
if cont == 1:
    print('Uau, você precisou de apenas {} tentativa para acertar, você é muito bom!'.format(cont))
else:
    print('Você acertou! Você precisou de {} tentativas para acertar!'.format(cont))