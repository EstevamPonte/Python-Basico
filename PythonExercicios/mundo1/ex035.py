r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmeento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima podem formar triangulo')
else:
  print('Os segmentos acima não podem formar triangulo')


