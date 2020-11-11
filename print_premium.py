def mensagem(msg):
    tamanho = len(msg) + 2
    print('~'*tamanho)
    print(f' {msg}')
    print('~'*tamanho)


msg = str(input('Digite aqui uma mensagem: '))
mensagem(msg)