#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
termo = p
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print ('FIM')
