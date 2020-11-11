from datetime import date
ano_atual = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
alistamento = nasc + 18
idade = ano_atual - nasc
while nasc > ano_atual:
    print('Muito engraçado, nem estamos nesse ano ainda, tente novamente, à sério.')
    nasc = int(input('Digite o ano em que você nasceu, espertinho: '))
else:
    sexo = int(input('Qual seu sexo?\n[1] - Feminino\n[2] - Masculino '))
    if sexo == 1:
        print('Oh, você é uma garota, não precisa se alistar a não sei que queira!')
    elif sexo == 2 and alistamento >= ano_atual and idade <= 18:
        print('Você nasceu em {}\nSeu alistamento será em {}\nFalta(m) {} ano(s) para seu alistamento!'.format(nasc, alistamento, (18 - idade)))
    elif sexo == 2 and alistamento < ano_atual and idade > 18:
        print('Você nasceu em {}, seu alistamento deveria ter ocorrido em {}, se não fez, apresse-se em fazer'.format(nasc, alistamento))
    else:
        print('A opção digitada é inválida.')