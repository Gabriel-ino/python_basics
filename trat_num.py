num = int(input('Digite quantos números inteiros quiser, para sair, digite 999: '))
cont = 0
som = 0
while num != 999:
    cont += 1
    som += num
    num = int(input('Digite quantos números inteiros quiser, para sair, digite 999: '))
print('Você digitou {} números e a soma entre os números digitados é: {}'.format(cont, som))
