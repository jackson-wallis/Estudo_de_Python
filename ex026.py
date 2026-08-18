from random import randint
computador = randint(0, 5)
print ('-=-' * 20)
print ('Vou pensar em um número entre 1 a 5. TENTE ADVINHAR...')
print ('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
if jogador == computador:
    print ('Parabéns, acertou!')
else:
    print ('Errou, eu escolhi o {} e não o {}, tente novamente!'.format(computador, jogador))