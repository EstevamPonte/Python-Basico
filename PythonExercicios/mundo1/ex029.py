velocidade = float(input('Digite sua quilometragem'))
if velocidade > 80:
  print('Voce ultrapassou 80km/h voce recebeu uma multa de {:.2f} reais'.format((velocidade - 80) * 7))
