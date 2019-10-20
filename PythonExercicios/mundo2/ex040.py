nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if 7 > media >= 5:
    print('o aluno esta em recuperação com a media {}'.format(media))
elif media < 5:
    print('O aluno esta reprovado com a media {}'.format(media))
else:
    print('o aluno passou com media {}'.format(media))
