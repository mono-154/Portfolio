print('(1)')
for i in range(1,16):
  if i % 2 == 1:
    print(i,end =' ')
  
print('\n\n(2)')
for i in range(2,31,2):
  if i % 10 == 0:
    print(i)
  else:
    print('%2d'  % i,end=' ')

print('\n(3)')
for i in range(1,10):
  for j in range(i,10):
    print(j, end=' ')
  print(' ')