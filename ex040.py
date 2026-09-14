#Criação de um jogo de Jonkepô, importando a biblioteca random, para que o computador escolha um valor aleatório

import random
import time # Foi importado a biblioteca time, para a usar o componente sleep(), fazendo com que haja uma espera de tempo de acordo com o número que for colocado dentro do ()
itens = ('PEDRA','PAPEL', 'TESOURA')
computador = random.randint(0, 2)
print ('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
time.sleep(1) # atraso de 1 segundo
print('KEN')
time.sleep(1) # atraso de 1 segundo
print('PO')
time.sleep(1) # atraso de 1 segundo
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')