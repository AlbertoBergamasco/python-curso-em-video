from math import trunc

num = float(input('Digite um valor: '))

print('o valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
print('tambem pode ser feito com "int(num) {}"'.format(int(num)))

