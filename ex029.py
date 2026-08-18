distancia = float(input('Qual a distância da sua viagem? '))
print ('Você está prestes a iniciar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print ('O preço da sua viagem será de R${:.2f}'.format(preço))