from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
res = 0
print('O que você quer fazer com esses números?')
opc = int(input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Novos números\n[5] - Sair'))
while opc != 5:
    while opc == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
        opc = int(input('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Novos números\n[5] - Sair'))
    if opc == 1:
        res = n1+n2
        print(res)
        sleep(4.5)
    if opc == 2:
        res = n1 - n2
        print(res)
        sleep(4.5)
    if opc == 3:
        res = n1 * n2
        print(res)
        sleep(4.5)
    opc = int(input('O que você quer fazer agora?\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Novos números\n[5] - Sair'))
