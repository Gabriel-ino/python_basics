while True:
    cont = 0
    num = int(input('Digite aqui um número: '))
    if num < 0:
        print('Programa encerrado!')
        break
    while cont <= 10:

        print(f'{num} x {cont} = {num * cont}')
        cont += 1