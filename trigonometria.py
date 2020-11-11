import math
CO = float(input('Programa para calcular a hipotenusa de um triângulo\nDigite o comprimento do cateto oposto: '))
CA = float(input('\nAgora, digite o cateto adjacente: '))
hip = pow(CO, 2) + pow(CA, 2)
print('A hipotenusa do triângulo é: {:.2f} '.format(math.sqrt(hip)))
HIP = math.sqrt(hip)
sen = CO / HIP
cos = CA / HIP
tg = CO / CA
print('O seno do triângulo vale {:.2f}, o cosseno vale {:.2f} e a tangente {:.2f}'.format(sen, cos, tg))