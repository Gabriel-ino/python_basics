lista = str(input('Digite aqui sua expressão:'))
if lista.index(')') < lista.index('('):
    print('Sua expressão está errada!')
else:
    if lista.count('(') == lista.count(')'):
        print('Sua expressão está correta!')
    else:
        print('Sua expressão está errada!')