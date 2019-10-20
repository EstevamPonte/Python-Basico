from datetime import date
nascimento = int(input('Digite seu ano de nacimento: '))
idade = date.today().year - nascimento

if idade < 18:
    print('Nao esta na hora de se alistar, falta {} anos'.format((18 - idade)))
elif idade > 18:
    print('Voce está {} anos atrasado para se alistar'.format((idade - 18)))
else:
    print('Voce precisa se alistar esse ano')