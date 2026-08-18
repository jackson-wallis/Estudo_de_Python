velocidade = int(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print ('MULTADO! Você ultrapassou o limite da via de 80km/h')
    multa = (velocidade - 80) * 7
    print ('Você deve pagar uma multa de R${:.2f}'.format(multa))
print ('Dirija com segurança!!!')


