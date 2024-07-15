n = float(input('Digite o valor do produto: '))
d = float(input('Digite o valor do desconto em porcentagem: '))

d = n*(d/100)
t = n-d

print('O valor do produto é {:.2f}'.format(n))
print('O valor do desconto é {:.2f}'.format(d))
print('O valor total com desconto fica {:.2f}'.format(t))