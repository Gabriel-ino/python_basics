from termcolor import colored
ano = int(input(colored('Digite um ano qualquer: ', 'magenta')))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(colored('O ano {} é bissexto!'.format(ano),'green'))
else:
    print(colored('O ano {} não é bissexto!'.format(ano), 'red'))