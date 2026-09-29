#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
pessoa_maior = 0 #precisa guardar também qual pessoa teve o maior e o menor peso
pessoa_menor = 0 #precisa guardar também qual pessoa teve o maior e o menor peso
for pessoa in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
        pessoa_maior = pessoa
        pessoa_menor = pessoa
    else:
        if peso > maior:
            maior = peso
            pessoa_maior = pessoa
        if peso < menor:
            menor = peso
            pessoa_menor
print('A {}ª pessoa possui maior peso, pesando {}kg'.format(pessoa_maior, maior))
print('A {}ª pessoa possui menor peso, pesando {}kg'.format(pessoa_menor, menor))
