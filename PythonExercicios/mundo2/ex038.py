primeiro = int(input('digite um valor: '))
segundo = int(input('digite um valor: '))

if segundo > primeiro:
    print('o numero {} é maior que o numero {}'.format(segundo, primeiro))
elif primeiro > segundo:
    print('o numero {} é maior que o numero {}'.format(primeiro, segundo))
else:
    print('Os dois numeros sao iguails')