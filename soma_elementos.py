lista = []
cont = 0
som = 0
while True:
    x = float(input('Digite aqui um número (tecle 0000 para parar): '))
    if x == 0000:
        break
    lista.append(x)
    cont += 1
    som += x

print(f'Os números digitados foram {lista}, o somatório entre eles é {som}')
