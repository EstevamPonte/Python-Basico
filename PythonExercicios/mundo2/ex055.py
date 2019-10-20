pesado = 0
leve = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        elif peso < leve:
            leve = peso
print('O mais leve é {} e o mais pesado é {}'.format(leve, pesado))