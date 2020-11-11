cont = 0
fib = 1
ant = 0
tot = int(input('Quantos números da sequência fibonacci você quer?'))
while cont < tot:
    while cont == 0:
        fib += ant
        cont += 1
        print(fib, end='->')
    if cont != 0:
        fib += ant
        ant = fib - ant
        cont += 1
        print(fib, end='->')
print('FIM!')
