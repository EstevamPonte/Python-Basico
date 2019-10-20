from random import randint
from time import sleep
aleatorio = randint(0, 5)
adivinha = int(input('Tente adivinhar: '))
print('PROCESSANDO...')
sleep(3)
if adivinha == aleatorio:
  print('Parabens, voce venceu')
else:
  print('Tente de novo, voce perdeu')