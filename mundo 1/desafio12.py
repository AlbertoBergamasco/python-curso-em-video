l = float(input('Digite a largura da parede: '))
d = float(input('Digite a altura da parede: '))
area = l * d
tinta = area / 2

print('Para pintar uma parede com {}m2, eu preciso de {} litros de tinta.'.format(area, tinta))