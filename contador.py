from time import sleep


def cont(ini, fim, passo):
    conta_passo = ini
    print('Processando contagem', end='')
    for c in range(0, 3):
        print('.', end='')
        sleep(1.5)
    print('\n')
    if ini <= fim:
        while conta_passo <= fim:
            print(conta_passo, end=' ')
            conta_passo += passo
            sleep(1)
        print('\n')
    else:
        while conta_passo >= fim:
            print(conta_passo, end=' ')
            conta_passo -= passo
            sleep(1)


cont(1, 10, 1)
cont(10, 0, 2)
print('\nSua vez! ')
while True:
    i = int(input('Digite o número de início: '))
    f = int(input('Digite o número final: '))
    p = int(input('De quantos em quantos números você quer fazer? '))
    cont(i, f, p)
    esc = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Valor inválido. Quer continuar [S/N]? ')).strip().upper()[0]
    if esc == 'N':
        break




