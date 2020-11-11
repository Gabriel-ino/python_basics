from termcolor import colored
num = int(input('Digite aqui um número qualquer: '))
cont = 0

for c in range (1, num + 1):
    if num % c == 0:
        print(colored(c, 'green'))
        cont += 1
    else:
        print(colored(c, 'red'))

print('O número {} foi dividido {} vezes'.format(num, cont))
if cont == 2:
    print('Por isso ele é primo')