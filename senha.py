
senha = str(input('Crie uma senha: '))
cont = 1
while True:
    ent = str(input('Digite aqui a sua senha para entrar:'))
    while ent != senha:
        ent = str(input('Senha errada, tente novamente.'))
        cont += 1
        if cont > 3:
            print('BLOQUEADO! VOCÊ ESTÁ IMPEDIDO DE ACESSAR.')
            quit()
    if ent == senha:
        print('Senha correta, seja bem-vindo.')
        break


print(f'Você precisou de {cont} tentativas para acertar sua senha')