num_ex = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:

    num = (int(input('Digite aqui um número entre 0 e 20: ')))
    print(f'O número que você digitou foi: {num_ex[num]}')
    esc = str(input('Você quer continuar [S/N]?')).strip().upper()[0]
    if esc == 'N':
        break

print('Volte sempre!')
