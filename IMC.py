from termcolor import colored
peso = float(input(colored('Digite aqui o seu peso: ', 'magenta')))
h = float(input(colored("Agora, digite sua altura: ")))
IMC = peso / (h * h)
if IMC < 18.5:
    print(colored('Você está abaixo do peso ideal!', 'red'))
elif IMC >=18.5 and IMC <=25:
    print(colored('Você está no peso ideal! Parabéns!', 'green'))
elif IMC > 25 and IMC <=30:
    print(colored('Você está com sobrepeso, cuidado com sua saúde!', 'yellow'))
elif IMC >30 and IMC <=40:
    print(colored('Você está com obesidade, cuidado com sua saúde.', 'red'))
else:
    print(colored('OBESIDADE MÓRBIDA, PROCURE UM MÉDICO!', 'red'))