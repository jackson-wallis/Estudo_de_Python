#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
print('Informe dois valores abaixo, para que eu possa realizar a operação desejada')
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

opção = 0

while opção != 5:
    opção = int(input('''Selecione abaixo a opção desejada:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    '''))
    if opção == 1:
        print('A soma dos dois valores é igual a {}'.format(valor1 + valor2))
    elif opção == 2:
        print('A multiplicação dos dois valores é igual a {}'.format(valor1 * valor2))
    elif opção == 3:
        print(max(valor1, valor2))
    elif  opção == 4:
        valor1 = int(input('Informe o novo primeiro valor: '))
        valor2 = int(input('Informe o novo segundo valor: '))
else:
    print('Fim do programa...')


