lista1 = []
cad = []
pmaior = pmenor = 0
while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    if len(cad) == 0:
        pmaior = pmenor = lista1[1]
    else:
        if lista1[1] > pmaior:
            pmaior = lista1[1]
        if lista1[1] < pmenor:
            pmenor = lista1[1]
    cad.append(lista1[:])
    lista1.clear()
    esc = str(input('Quer continuar? [S/N]')).strip().upper()
    while esc not in 'SN':
        esc = str(input('Valor inválido. Quer continuar? [S/N]')).strip().upper()
    if esc == 'N':
        break
print(f'Você cadastrou {len(cad)} pessoas.\nOs cadastros foram {cad}\nO maior peso é {pmaior}\nO menor peso é {pmenor}')
