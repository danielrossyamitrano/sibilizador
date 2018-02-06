from silabilizador import Silabilizador
s = Silabilizador()

lista = s('cigüeña')
for i, item in enumerate(lista):
    if i != len(lista) - 1:
        print(item, '-', sep='', end='')
    else:
        print(item)
