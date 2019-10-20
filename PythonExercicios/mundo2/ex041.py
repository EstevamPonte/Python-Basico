from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')