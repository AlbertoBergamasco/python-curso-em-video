import math

c1 = float(input('Digite o primeiro cateto: '))
c2 = float(input('Digite o segundo cateto: '))

h = math.sqrt((c1*c1)+(c2*c2))
print('Com os valores c1:{:.2f}, c2:{:.2f} '.format(c1, c2))
print('A hipotenusa vai medir {:.2f}'.format(h))