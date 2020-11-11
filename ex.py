lista = (int(input('Digite aqui um valor: ')),
        int(input('Digite aqui um valor: ')),
        int(input('Digite aqui um valor: ')),
        int(input('Digite aqui um valor: ')))

print(f'Você digitou ou números {lista}')
print(f'O valor 3 aparece na posição {lista.index(3+1)}')
print(f'O valor 9 aparece {lista.count(9)} vez(es)')

for num in lista:
    if num % 2 == 0:
        print(f'O número {num} é par')
