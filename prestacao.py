from termcolor import colored
val = float(input(colored('Digite aqui o valor da casa: ', 'magenta')))
sal = float(input(colored('Digite aqui o salário do comprador: ', 'magenta')))
year = int (input(colored('Digite aqui em quantos anos a casa será paga: ', 'magenta')))
prest = val / (year * 12.0)
print(colored('Valor da casa:R${:.2f}\nO valor da prestação mensal é de:R${:.2f}\nO salário é:R${:.2f}'.format(val, prest, sal)))
if prest <= 0.3 * sal:
    print(colored('Pagamento aceito! Prestação mensal não excede o limite de 30% do salário', 'green'))
elif prest > 0.3 * sal:
    print(colored('Pagamento negado! Valor da prestação excede limite de 30% do salário.', 'red'))
