from datetime import date
nasc = int(input('Digite o ano em que o atleta nasceu: '))
idade = date.today().year - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('A categoria do atleta é MIRIM')
elif idade > 9 and idade <=14:
    print('A categoria do atleta é INFANTIL')
elif idade > 14 and idade <=19:
    print('A categoria do atleta é JUNIOR')
elif idade > 19 and idade <=25:
    print('A categoria do atleta é SÊNIOR')
else:
    print('A categoria do atleta é MASTER')