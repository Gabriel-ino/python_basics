from termcolor import colored
print(colored('-='*20, 'blue'))
print(colored('Analisador de triângulos', 'blue'))
print(colored('-='*20, 'blue'))
seg_1 = float(input(colored('Digite aqui o primeiro segmento do triângulo: ', 'magenta')))
seg_2 = float(input(colored('Digite aqui o segundo segmento do triângulo: ', 'magenta')))
seg_3 = float(input(colored('Digite aqui o terceiro segmento do triângulo: ', 'magenta')))

if seg_1 + seg_2 > seg_3 and seg_1 + seg_3 > seg_2 and seg_2 + seg_3 > seg_1:
    print(colored('\n---De acordo com os segmentos, É um triângulo!---', 'green'))
    if seg_1 == seg_2 == seg_3:
        print(colored('---Tipo de triângulo: Equilátero---', 'green'))
    elif seg_1 == seg_2 != seg_3 or seg_1 == seg_3 != seg_2 or seg_3 == seg_2 != seg_1:
        print(colored('---Tipo de triângulo: Isósceles---', 'green'))
    else:
        print(colored('---Tipo de triângulo: Escaleno---', 'green'))



else:
    print(colored('\n---De acordo com os segmentos, NÃO É um triângulo!---', 'red'))