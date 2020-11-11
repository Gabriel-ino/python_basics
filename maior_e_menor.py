lista = []
media = 0
for c in range(0, 10):
    val = float(input('Digite aqui um valor: '))
    lista.append(val)
    media += val / 10
    if c == 0:
        maior = val
        menor = val
    if val > maior:
        maior = val
    if val < menor:
        menor = val
print(f'Os valores digitados foram {lista}\nO menor valor é {menor}\nO maior valor é {maior}'
      f'\nA média entre os valores é {media}')
