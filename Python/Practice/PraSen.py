print('(1)')

for i in range(1,12):
  for j in range(i,11):
    
    print("*", end='')
  print('')

print('\n(2)')

for i in range(0,10,1):
  for j in range(0,10,1):
    start = int(i)
    if j >= start:
      print("*",end="")
    else:
      print(' ',end="")
  for k in range(0,10,1):
    end = int((10-i)-1)
    if k >= end:
      print('*',end='')
    else:
      print('',end='')
  print("")

print('\n(3)')

for i in range(0,10,1):
  for j in range(0,10,1):
    start = int(i)
    if j >= start:
      print("*",end="")
    else:
      print(' ',end="")
  print("")
  

print("\n(4)")

for i in range(0, 10, 1):
  for j in range(0, 10*2-1, 1):
    start = int(i)
    end = int(2*(10-1)-i)
    if j >= start and j <= end:
      print("*", end="")
    else:
      print(" ", end="")
  print("")