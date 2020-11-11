print('=-'*20)
print('10 TERMOS DE UMA PROGRESÃO ARITMÉTICA')
print('=-'*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = t + (10-1) * r
for c in range(t, décimo + r, r):
    print('{}'.format(c), end='->')
print('Fim')