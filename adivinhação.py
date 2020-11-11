from random import randint
from time import sleep
b = randint(0, 5)
a = int(input('Vou pensar em um número inteiro entre 0 e 5, tente adivinhar qual é!\nDigite:'))
print('Vamos ver...')
sleep(2.0)
if a == b:
    print('Você acertou! Eu pensei exatamente {}!'.format(b))
else:
    print('Que pena! Você errou, o número em que pensei foi: {}'.format(b))