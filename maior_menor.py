
n1 = float(input('Digite aqui um valor qualquer: '))
n2 = float(input('Digite aqui outro valor qualquer: '))
print('-='*20, '\nOs valores digitados foram: {} e {}'.format(n1, n2))
if n1 > n2:
    print('Dentre eles, o maior valor é: {}'.format(n1))
elif n2 > n1:
    print('Dentre eles, o maior valor é: {}'.format(n2))
else:
    print('Os dois valores são iguais!')
print('-='*20)