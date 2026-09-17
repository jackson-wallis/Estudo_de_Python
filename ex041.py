#exercício sobre a aula de laços de repetição, usando o for
#Exemplo
#for c in range(1,10):
   # print('Hello, world!')

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time # Aqui eu importei a biblioteca para usar a função time.sleep(), para reduzir o tempo da contagem em 1s
print('-=' * 10)
print('Contagem regressiva para os fogos de artifícios')
print('-=' * 10)
for c in range(10, 0, -1): # O (-1) dentro do () significa que a contagem é ordem regressiva
    print(c)
    time.sleep(1)
print('BOOM, BOOM, POWW')
