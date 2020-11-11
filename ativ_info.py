
def converttobin(n):
    listabin.append(bin(n))


def converttooct(n):
    listaoct.append(oct(n))


def converttohex(n):
    listahex.append(hex(n))


cont = 0
listadec = []
listaoct = []
listahex = []
listabin = []
while True:
    num = int(input('Digite aqui um número inteiro: '))
    listadec.append(num)
    converttobin(num)
    converttohex(num)
    converttooct(num)
    cont += 1
    esc = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Valor inválido. Quer continuar [S/N]?')).strip().upper()[0]
    if esc == 'N':
        break
print(' Decimal', end='  ')
print(' Octal', end='  ')
print(' Hexadecimal', end='  ')
print(' Binário', end='  ')
print('\n')
print('-' * 9, end=' ')
print('-'*7, end=' ')
print('-'*13, end=' ')
print('-'*9, end=' ')

for c in range(0, cont):
    print(f'\n\n   {listadec[c]}        {listaoct[c]}        {listahex[c]}        {listabin[c]}\n')
print(end=' ')


