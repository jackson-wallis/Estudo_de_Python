from datetime import date

print('Você será direcionado para a sua categoria na Confederação Nacional de Natação de acordo com a sua idade')
atleta = int(input('Informe o seu ano de nascimento: '))
ano = date.today().year
idade = ano - atleta
if idade <= 9:
    print('A sua categoria será: MIRIM')
elif idade == 10 and idade < 14:
    print('A sua categoria será: INFANTIL')
elif idade == 15 and idade < 19:
    print('A sua categoira será: JÚNIOR')
elif idade == 20 and idade < 25:
    print('A sua categoria será: SÊNIOR')
else: idade >= 25
print('A sua categoria será: MASTER')
