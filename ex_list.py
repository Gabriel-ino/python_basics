lista = []
for c in range (0, 5):
    num = float(input('Digite aqui um valor qualquer: '))
    lista.append(num)
print(f'Os números digitados foram: {lista}\nO maior valor é: {max(lista)}\nO menor valor é: {min(lista)}')
