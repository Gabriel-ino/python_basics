from numpy import random
print('-='*20)
print('PAR OU IMPAR')
print('-='*20)
vit = 0
der = 0
while True:

    num = int(input('Diga um valor: '))
    num_2 = random.randint(0,10)
    esc = str(input('Par ou ímpar?')).strip().upper()[0]
    print(f'Eu escolhi {num_2}')
    print(f'A soma de {num} e {num_2} dá {num + num_2}')
    if esc == 'P':
        if (num + num_2) % 2 == 0:
            print('Você venceu! Vamos novamente')
            vit += 1
        else:
            print('Que pena, você perdeu')
            der += 1
            break
    if esc == 'I' or esc == 'Í':
        if (num + num_2) % 2 != 0:
            print('Você venceu! Vamos novamente')
            vit += 1
        else:
            print('Que pena, você perdeu')
            der += 1
            break
print(f'Você teve um total de {vit} vitória(s) e {der} derrota(s)')



