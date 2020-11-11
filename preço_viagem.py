from termcolor import colored
d = float(input(colored('Digite a quilometragem da sua viagem: ', 'magenta')))

if d <= 200:
    ticket = 0.5 * d
else:
    ticket = 0.45 * d
ticket = str(ticket)
print(('O valor da sua passagem é de:{}'.format(colored('R$' + ticket, 'cyan'))))
