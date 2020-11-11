som = 0
for c in range (0, 6):
    num = int(input('Digite um valor inteiro qualquer: '))
    if num % 2 == 0:
        som += num
print('O somatório dos valores pares é: {}'.format(som))