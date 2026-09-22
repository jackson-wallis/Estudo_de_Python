#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input("Digite um número para ver a sua tabuada: "))
for c in range(0, 11):
    print("{} * {:2} = {}".format(num, c, num * c))