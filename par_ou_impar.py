from termcolor import colored
n = int(input(colored('Digite um numero inteiro qualquer: ', 'magenta')))
if n%2 == 0:
    print('O número é {}'.format(colored('PAR', 'cyan')))
else:
    print('O número é {}'.format(colored('IMPAR', 'cyan')))