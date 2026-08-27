# As duas variáveis eu usei o float, pois a nota poderia não ser um número inteiro
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
# Observe-se a ordem de precedência, primeiro o valor vai ser calculado dentro dos () e posteriormente será divido pelo / 2
média = (n1 + n2) / 2
print('Sua nota final é {}'.format(média))
if média >= 7:
    print('Parabéns Aprovado!!!')
elif média == 5 or média <= 6.9:
    print('Recuperação!!!')
elif média < 5:
    print('Reprovado!!!')

