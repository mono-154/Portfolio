import random

def janken(x):
  result = {'g':0,'c':1,'p':2}
  return result[x]

print('じゃんけんゲーム')
cnt= gU = gP = 0
while True:
  cnt += 1
  user = input('Choose one of (g,c,p):')
  pc = random.choice(['g', 'c', 'p'])
  print('You = %s, PC = %s, so . . ' % (user,pc), end=' ')
  winner = janken(user) - janken(pc)
  if winner == 2 or winner == -1:
    print('You won!')
    gU+=1
  elif winner == 1 or winner == -2:
    print('You lost. .')
    gP += 1
  else:
    print('Even!')
  if cnt > 4 or gU > 2 or  gP > 2:
    break
print('You = %d, PC = %d' % (gU,gP))