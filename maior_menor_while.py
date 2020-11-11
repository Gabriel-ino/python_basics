num = float(input('Digite um valor qualquer: '))
maior = num
menor = num
pg = str(input('Você quer continuar digitando valores?')).upper().strip()[0]
while pg == 'S':
    num = float(input('Digite um valor qualquer: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    pg = str(input('Você quer continuar digitando valores?')).upper().strip()[0]

print('O maior valor é: {}\nO menor valor é: {}'.format(maior, menor))
