nome = str(input('Digite aqui o seu nome: ')).strip()
print('Seu nome é: {}\nEm maiúsculo: {}\n'
      'Em minúsculo: {}\nQuantidade de letras: {}'.format(nome, nome.upper(), nome.lower(), len(nome) - nome.count(' ')))