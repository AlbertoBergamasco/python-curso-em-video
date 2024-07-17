d = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos km foi rodado com o carro alugado?'))

preco = (d * 60) + (km * 0.15)

print('O valor total a ser pago é {}'.format(preco))