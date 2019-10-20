nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Prazer em te conhecer!!!')
print('Seu primeiro nome é {}'.format(lista[0]))
tamanho = len(lista) - 1
print('Seu ultimo nome é {}'.format(lista[tamanho]))
