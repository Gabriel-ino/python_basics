from random import randint
num = int(input('Quantos jogos você quer que eu sorteie?'))
lista = []
prob = (1/50063860) * num
for i in range(0, num):
    for c in range(0, 6):
        lista.append(randint(0, 60))
    print(lista)
    lista.clear()
print(f'Você tem uma probabilidade de {prob:.7f} % de ganhar')

