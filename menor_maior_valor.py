from termcolor import colored
sal = float(input(colored('Digite aqui o salário do funcionário: ', 'magenta')))
if sal <= 1250:
    sal = sal + 0.15 * sal
else:
    sal = sal + 0.1 * sal

sal = str(sal)
print("O salário do funcionário passará a ser: {}".format(colored('R$' + sal, 'green')))
