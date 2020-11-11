maior = 0
menor = 0
qtd = int(input('Digite a quantidade de pessoas a serem analisadas: '))
for c in range (0, qtd):
    peso = float(input('Digite aqui o peso da pessoa {}: '.format(c)))
    if c == 0:
        maior = peso
        menor = peso

    elif peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(maior, menor)