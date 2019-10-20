from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    if atual - ano < 21:
        menor += 1
    else:
        maior += 1
print('Existe {} pessoas de maior'.format(maior))
print('Existe {} pessoas de menor'.format(menor))
