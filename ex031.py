nome = str(input("Informe o seu nome a seguir:"))
casa = float(input("Qual é o valor da casa que o sr(a): {}, deseja negociar? " .format(nome)))
salario = float(input("Qual o seu salário atual? "))
anos = int(input("Em quantos anos deseja quitar o valor? "))
mensal = casa / anos / 12
print ("A prestação mensal ficaria no valor de R${:.2f}".format(mensal))
if mensal > salario * 30 / 100:
    print("Emprestimo negado!")
else:
    print("Emprestimo aprovado!!!")