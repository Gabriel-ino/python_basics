from termcolor import colored
n1 = float(input('Digite a N1 do aluno: '))
while n1 > 10:
    n1 = float(input('Nota errada. Digite novamente: '))
n2 = float(input('Digite a N2 do aluno: '))
while n2>10:
    n2 = float(input('Nota errada. Digite novamente: '))
media = (2*n1 + 3*n2) / 5
print('Média do aluno: {}'.format(media))
if media >= 6.0:
    print(colored('Aluno aprovado!', 'green'))
elif media < 6.0 and media >= 4.0:
    print(colored('Aluno de AF', 'yellow'))
else:
    print(colored('Aluno reprovado!', 'red'))