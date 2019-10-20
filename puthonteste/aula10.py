# nome = str(input('Qual seu nome? '))
# if nome == 'Estevam':
#   print('Seu nome é tão lindo')
# else:
#   print('Seu nome é tao normal')
# print('Bom dia {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('Sua media foi {}, parabens'.format(m))
else:
    print('Sua media foi {}, estude mais'.format(m))
