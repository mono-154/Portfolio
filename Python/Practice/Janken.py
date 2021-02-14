def janken(x):
  result = {'g':0,'c':-1,'p':1}
  return result[x]

print('じゃんけんゲーム')
cnt= gU = gP = 0
while True:
  cnt += 1
  user = input('Choose one of (g,c,p):')
  pc='g'
  print('You = %s, PC = %s, so . . ' % (user,pc), end=' ')
  winner = janken(user)
  if winner == 1:
    print('You won!')
  elif winner == 0:
    print('Even!')
  else:
    print('You lost. .')
    gP += 1
  if cnt > 4 or gU > 2 or  gP > 2:
    break
print('You = %d, PC = %d' % (gU,gP))