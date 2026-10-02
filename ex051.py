#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher = 0
for pessoa in range(1,5):
    pessoa = print('----Pessoa {}----'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Fm' and idade < 20:
        totmulher += 1

médiaidade = somaidade / 4
print('A média da idade do grupo é {} anos'.format(médiaidade))
print('O homem mais velho do grupo se chama {} e têm {} anos'.format(nomemaisvelho, maioridadehomem))
print('A todo possui {} mulheres com menos de 20 anos no gru po'.format(totmulher))