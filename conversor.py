from termcolor import colored
n = int(input(colored('Digite aqui um número inteiro: ', 'magenta')))
print(colored('-='*20, 'magenta'))
print(colored('\nEscolha a conversão:\n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\n', 'blue'))
print(colored('-='*20, 'magenta'))
dig = int(input(colored('Qual conversão você deseja fazer?')))
if dig == 1:
    print('O número {num} em binário é: {num: b}')
elif dig == 2:
    print('O número {} em octal é {}'.format(n, oct(n)))
