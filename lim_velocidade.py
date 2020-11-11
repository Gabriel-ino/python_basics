from termcolor import colored
v = float(input('Qual a velocidade do veículo?'))
if v <= 80.0:
    print('Velocidade permitida. Tenha um bom dia!')
else:
    multa = float((v - 80) * 7)
    print(colored('Você ultrapassou o limite de 80 Km/h, e recebeu uma multa de R${:.2f}'.format(multa), 'red'))