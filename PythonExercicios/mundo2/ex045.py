from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 10)
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('-=' * 10)

if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('Jogada invalida')

else:
    print('Invalidooo')