import datetime
cad = {'nome': str(input('Nome:'))}
nasc = int(input('Ano de nascimento: '))
cad['idade'] = datetime.date.today().year - nasc
cad['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if cad['ctps'] != 0:
       cad['contrato'] = int(input('Ano início de contratação: '))
       cad['salário'] = float(input('Salário: '))
       cad['aposentadoria'] = cad['idade'] + (cad['contrato'] + 35) - datetime.date.today().year

for k, v in cad.items():
       print(f'O {k} tem valor {v}')

