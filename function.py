def terreno(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno é de: {a} m²')


l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
terreno(l, c)