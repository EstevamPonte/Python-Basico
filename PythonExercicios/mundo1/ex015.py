dias = int(input('quantos dias rodados? '))
km = float(input('Quantos km rodados'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(pago))