s=0
cont2 = 0
for cont in range (1, 501, 2):
    if cont % 3 == 0:
        cont2 += 1
        s += cont
print('A soma dos {} valores solictados é {}'.format(cont2, s))