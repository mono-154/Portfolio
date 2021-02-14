while True:
  buttom=input('底辺の長さは？:')
  if len(buttom)==0:
    break
  buttom=float(buttom)
  height=float(input('高さは？:'))

  area=buttom * height / 2
  break
print('この三角形の面積は'+'%.1f'  % area+ 'です')