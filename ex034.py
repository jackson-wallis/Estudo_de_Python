# Aqui eu realizei a importação da classe date do módulo datetime (bibliotecas)
from datetime import date

# A expressão date.today() traz o valor da data exata(dia, mês e ano) porém ao colocar o (.year), a expressão traz somente o ano
atual = date.today().year

nasc  = int(input('Informe o ano em que você nasceu: '))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!!!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para você se alistar".format(saldo))
elif idade > 18:
    saldo = idade - 18
    print("Você deveria ter se alistado há {} anos".format(saldo))




