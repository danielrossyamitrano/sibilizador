from silabilizador import Silabilizador
s = Silabilizador()

lista = s('importantísimo')
for i, item in enumerate(lista):
    if i != len(lista) - 1:
        print(item, '-', sep='', end='')
    else:
        print(item)
