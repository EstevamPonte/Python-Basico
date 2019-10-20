somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher = 0
for p in range(1, 5):
    print('-------- {} PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    elif sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    elif sexo in 'Ff' and idade < 20:
        totMulher += 1
mediaIdade = somaIdade / 4
print('A media de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} e se chama {}'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo sao {} mulher com menos de 20 anos'.format(totMulher))