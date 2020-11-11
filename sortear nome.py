import random
qtd = int(input('Digite a quantidade de alunos: '))
cont = 0
lista = []
while cont < qtd:
    al = str(input('Digite o nome do(a) aluno(a): '))
    lista.append(al)
    cont = cont + 1
print('alunos:', lista)
print('O aluno escolhido foi: ', random.choice(lista))

