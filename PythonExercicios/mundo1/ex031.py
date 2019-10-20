distancia = float(input('Distância da viagem: '))
# if distancia <= 200:
#   print('O valor da passagem é: {} reais'.format(0.50*distancia))
# else:
#   print ('O valor da passagem é: {} reais'.format(0.45*distancia))

#ouu

preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
