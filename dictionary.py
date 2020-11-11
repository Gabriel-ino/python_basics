aluno = []
sit = {}
qtd_al = int(input('Digite a quantidade de alunos: '))
for al in range(0, qtd_al):
    aluno[0] = str(input('Digite aqui o nome da aluno(a): '))
    aluno[1] = float(input('Digite aqui a média do(a) aluno(a): '))
    if aluno[1] >= 6.0:
        aluno[2] = 'Aprovado!'
        sit.append(aluno['res'])
    else:
        aluno[2] = 'Reprovado!'
        sit.copy(aluno)
    sit.copy(aluno)



for c in range(0, qtd_al):
    print(sit[c])
