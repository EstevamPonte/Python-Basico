numero = int(input('me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
  print('numero {} é par'.format(numero))
else:
  print('numero {} é impar'.format(numero))