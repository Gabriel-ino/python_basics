frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')