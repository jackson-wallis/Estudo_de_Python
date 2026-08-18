import math
ang = float(input('Digite um ângulo que desejar: '))
sen = math.asin(math.radians(ang))
print ('O SENO do ângulo {} é: {:.2f}'.format(ang, sen))
cos = math.cos(math.radians(ang))
print ('O COSSENO do ângulo {} é: {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print ('A TANGENTE do ângulo {} é: {:.2f}'.format(ang, tan))
