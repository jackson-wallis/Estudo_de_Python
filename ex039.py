compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:   
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão ''')
opção = int(input('Qual a sua opção? '))
if opção == 1:
    total = compras - (compras * 10 / 100)
elif opção == 2:
    total = compras - (compras * 5 / 100)
elif opção == 3:
    total = compras
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = compras + (compras * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} no final COM JUROS'.format(compras, totalparc))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compras, total))
