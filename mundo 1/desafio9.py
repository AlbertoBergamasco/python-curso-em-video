d = int(input('Digite uma distância em metros: '))

km = d / 1000
hm = d / 100
dam = d / 10
cm = d * 100
mm = d * 1000

print('A distância de {} metros corresponde a {:.3f} km, {:.3f} hm, {:.3f} dam, {:.0f} cm e {:.0f} mm'
      .format(d, km, hm, dam, cm, mm))
