from random import choice
from termcolor import colored
lista = ['Pedra', 'Papel', 'Tesoura']
esc = int(input(colored('Escolha sua opção:\n[0] - Pedra\n[1] - Papel\n[2] - Tesoura', 'cyan')))
me = lista[esc]
adv = choice(lista)
print('Você escolheu: {}'.format(me))
print('Eu escolhi: {}'.format(adv))
if me == adv:
    print('Empate!')
elif me == 'Pedra' and adv == 'Tesoura' or me == 'Papel' and adv == 'Pedra' or me == 'Tesoura' and adv == 'Papel':
    print('Parabéns, você ganhou!')
else:
    print('Eu venci!')
