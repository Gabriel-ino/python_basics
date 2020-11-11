from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ')
for num in lista:
    print(f'{num}', end=' ')
print(f'\nO maior número é {max(lista)}')
print(f'O menor número é {min(lista)}')

