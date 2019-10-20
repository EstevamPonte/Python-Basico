print('{:^40}'.format('LOJAS ESTEVAM'))
preco = float(input('Preco das comprasa: R$'))
print(''' Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao
''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - ((preco * 10) / 100)
elif opcao == 2:
    total = preco - ((preco * 5) / 100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(
        totalParcelas, parcela))
else:
    total = preco
    print('Opção invalida')
print('Sua compra será de R${:.2f} vai custar R${:.2f} no final.'.format(
    preco, total))
