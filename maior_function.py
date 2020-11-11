from time import sleep


def maior(lst):
    mv = 0
    print('Analisando a lista', end='')
    for v in range(0, 3):
        print('.', end='')
        sleep(0.75)
    for c in lst:
        if c == lst[0]:
            mv = c
        elif c > mv:
            mv = c

    print(f'\nOs valores digitados foram: {lst}\nO maior valor digitado foi: {mv}')


lista = []
print('Programa para calcular o maior valor dentre os digitados')
qtd_num = int(input('Digite aqui a quantidade de números para serem digitados: '))
for c in range(0, qtd_num):
    lista.append(int(input('Digite aqui o valor: ')))
maior(lista)

