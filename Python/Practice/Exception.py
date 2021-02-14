x=float(input('x='))
y=float(input('y='))
try:
  z=x/y
  print('x /y = %.2f' %z)
except:
  print('y should not be set to 0.')