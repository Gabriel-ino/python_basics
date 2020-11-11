lista = []
while True:
    x = float(input('Digite aqui um valor: '))
    lista.append(x)
    esc = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Valor inválido. Quer continuar? [S/N]')).strip().upper()[0]
    if esc == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números\nA lista em ordem decrescente fica {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')