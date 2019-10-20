Salario = float(input('Qual seu salario? '))
casa = float(input('valor da casa? '))
anos = int(input('Quanto anos pretende pagar essa casa? '))

prestacao = casa / (anos * 12)
minimo = Salario * 30 / 100

if prestacao <= minimo:
    print('emprestimo pode ser concedido')
else:
    print('emprestimo negado')